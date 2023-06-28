import smart_open, json
import pandas as pd
from typing import Dict, List, Union
from itertools import chain
from functools import reduce
from toolz import pipe

S3_PATH = 'https://s3.eu-west-2.amazonaws.com/igl-public/tutorials-data/{}'

INST_META_VARS = [
    "id",
    "display_name",
    "country_code",
    "type",
    "homepage_url"
]
WORK_META_VARS = [
    "id",
    "doi",
    "display_name",
    "publication_year",
    "publication_date",
    "cited_by_count",
    "is_retracted"
]
VENUE_META_VARS = [
    "id",
    "display_name",
    "url"
]

def deinvert_abstract(inverted_abstract: Dict[str, List]) -> Union[str, None]:
    """Convert inverted abstract into normal abstract

    Args:
        inverted_abstract: a dict where the keys are words
        and the values lists of positions

    Returns:
        A str that reconstitutes the abstract or None if the deinvered abstract
        is empty

    """

    if len(inverted_abstract) == 0:
        return None
    else:

        abstr_empty = (max(chain(*inverted_abstract.values())) + 1) * [""]

        for word, pos in inverted_abstract.items():
            for p in pos:
                abstr_empty[p] = word

        return " ".join(abstr_empty)

def extract_obj_meta(oalex_object: Dict, meta_vars: List) -> Dict:
    """Extracts variables of interest from an OpenAlex object (eg work, insitution...)

    Args:
        oalex_object: an OpenAlex object
        meta_vars: a list of variables to extract

    Returns:
        A dict with the variables of interest
    """

    return {var: val for var, val in oalex_object.items() if var in meta_vars}

def extract_work_venue(work: Dict, venue_vars: List) -> Dict:
    """Extracts nested metadata about a publication venue

    Args:
        work: an OpenAlex work
        venue_vars: a list of variables to extract

    Returns:
        A dict with the variables of interest
    """

    return {
        f"venue_{var}": val
        for var, val in work["host_venue"].items()
        if var in venue_vars
    }

def make_inst_metadata(inst_list: List, meta_vars: List) -> pd.DataFrame:
    """Makes a df with metadata about oalex institutions

    Args:
        doc_list: list of oalex institutions
        meta_vars: list of variables to extract

    Returns
        A df with instit-level metadata
    """

    return pipe(
        inst_list,
        lambda list_of_dicts: [
            extract_obj_meta(
                d,
                meta_vars=meta_vars,
            )
            for d in list_of_dicts
        ],
        pd.DataFrame,
    )

def make_work_metadata(work: Dict) -> Dict:
    """Extracts metadata about a work"""

    return {
        **extract_obj_meta(work, meta_vars=WORK_META_VARS),
        **extract_work_venue(work, venue_vars=VENUE_META_VARS),
    }

def make_work_corpus_metadata(works_list: List) -> pd.DataFrame:
    """Makes a df with work metadata

    Args:
        work_list: list of oalex works

    Returns:
        A df with work-level metadata
    """

    return pipe(
        works_list,
        lambda list_of_dicts: [make_work_metadata(pd.Series(d)) for d in list_of_dicts],
        pd.DataFrame,
    ).rename(columns={"id": "work_id"})

def get_nested_vars(work: Dict, variable: str, keys_to_keep: List) -> Union[None, List]:
    """Extracts nested variables from a document

    Args:
        doc: an open alex work
        nested_variable: the nested variable to extract
        keys_to_keep: the keys to keep in the nested variable

    Returns:
        A list of dicts with the nested variables
    """

    if variable not in work.keys():
        return None
    else:
        return [
            {
                **{"work_id": work["id"]},
                **{k: v for k, v in conc.items() if k in keys_to_keep},
            }
            for conc in work[variable]
        ]

def make_work_concepts(
    works_list: List,
    variable: str = "concepts",
    keys_to_keep: List = ["id", "display_name", "score"],
    make_df: bool = True,
) -> pd.DataFrame:
    """
    Extracts concepts from work (could be openalex or mesh)

    Args:
        doc_list: list of openalex
        variable: concept variable to extract
        keys_to_keep: keys to keep in the concept
        make_df: whether to make a df or not

    Returns:
        A df with work-level concepts

    """

    return pipe(
        works_list,
        lambda doc_list: [
            get_nested_vars(doc, variable=variable, keys_to_keep=keys_to_keep)
            for doc in doc_list
        ],
        lambda dict_list: pd.DataFrame(chain(*dict_list))
        if make_df
        else chain(*dict_list),
    )

def get_authorships(work: Dict) -> List:
    """
    Extract authorships from a document

    Args:
        work: an openalex

    Returns:
        A list of parsed dicts with the authors and their affiliations
    """
    return list(
        chain(
            *[
                [
                    {
                        **{"id": work["id"]},
                        **{f"auth_{k}": v for k, v in auth["author"].items()},
                        **{"affiliation_string": auth["raw_affiliation_string"]},
                        **{f"inst_{k}": v for k, v in inst.items() if k == "id"},
                    }
                    for inst in auth[
                        "institutions"
                    ]  # Some authors are affiliated to more than
                    # one institution.
                ]
                for auth in work["authorships"]
            ]
        )
    )

def make_work_authorships(works_list: List) -> pd.DataFrame:
    """
    Creates a df with authors and institutions per works

    Args:
        works_list: list of openalex works
    """

    return pipe(
        works_list,
        lambda list_of_docs: [get_authorships(doc) for doc in list_of_docs],
        lambda extracted: pd.DataFrame(chain(*extracted)),
    )

def make_citations(work_list: List) -> Dict:
    """Dict with the papers cited by each work"""

    return {doc["id"]: doc["referenced_works"] for doc in work_list}


def make_deinverted_abstracts(work_list: List) -> Dict:
    """Dict with the deinverted abstracts of each work (where available"""

    return pd.DataFrame.from_dict({
        doc["id"]: deinvert_abstract(doc["abstract_inverted_index"])
        if (type(doc["abstract_inverted_index"]) == dict)
        else None
        for doc in work_list
    }, orient='index').reset_index().rename(columns={0: 'deinverted_abstract', 'index': 'work_id'})

def cols_to_function():
    return {
        'work': make_work_corpus_metadata,
        'authorship': make_work_authorships,
        'concept': make_work_concepts,
        'inst': make_inst_metadata,
        'citation': make_citations,
        'deinverted_abstract': make_deinverted_abstracts
    }

def openalex(sample: bool = True, cols: Union[None, List[str]] = ['deinverted_abstract']):
    '''Loads the openalex dataset from S3. Cols here correspond to possible attributes to
    load. These are:
        'work': work-level metadata
        'authorship': authorship-level metadata
        'concept': concept-level metadata
        'inst': institution-level metadata
        'citation': citations
        'deinverted_abstract': deinverted abstracts

    Args:
        sample: whether to load the full dataset or a sample
        cols: which columns to load. If None, loads raw JSON. Column choices are
            'work', 'authorship', 'concept', 'inst', 'citation', 'deinverted_abstract'

    Returns:
        A df with the requested columns
    '''
    if not sample:
        key = 'openalex/openalex-gb-publications_year-2021.json'
    else:
        key = 'openalex/openalex-gb-publications_year-2021-sample.json'

    cols_dict = cols_to_function()

    with smart_open.open(S3_PATH.format(key)) as f:
        data = json.load(f)
        if cols is None:
            return data

    if isinstance(cols, str):
        return cols_dict[cols](data)
    
    dfs = []
    for col in cols:
        dfs.append(cols_dict[col](data))
    dfs = reduce(lambda left, right: pd.merge(left, right, on='work_id', suffixes=(False, '_drop')), dfs)
    return dfs[[col for col in dfs.columns if not col.endswith('_drop')]]
