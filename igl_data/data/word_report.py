from igl_data.data.s3_transfer import load_df_pkl
from igl_data.utilities import eval_cols
import smart_open
import pandas as pd

S3_PATH = 'https://s3.us-east-2.amazonaws.com/igl-public/dap-innovation-tutorials/{}'

def world_report_mesh(chunksize=50000):
    '''world_report_mesh
    Get a dataset of World Report projects that have abstracts and
    MeSH labels.

    Parameters
    ----------
    table : str
        Name of the table to load. Tables available include:
            - index
            - _id
            - _index
            - _score
            - coordinate_of_organisation.lat
            - coordinate_of_organisation.lon
            - cost_total_project
            - currency_total_cost
            - date_end_project
            - date_start_project
            - id_iso2_country
            - id_iso3_country
            - id_isoNumeric_country
            - id_of_continent
            - id_of_project
            - id_state_organisation
            - json_funding_project
            - placeName_city_organisation
            - placeName_continent_organisation
            - placeName_country_organisation
            - placeName_state_organisation
            - placeName_zipcode_organisation
            - rank_rhodonite_abstract
            - terms_descriptive_project
            - terms_mesh_abstract
            - terms_of_countryTags
            - textBody_abstract_project
            - textBody_descriptive_project
            - title_of_organisation
            - title_of_project
            - type_of_entity
            - year_fiscal_funding
            - _type
            - sort

    Returns
    -------
    DataFrame
        A dataframe with containing the World Report projects with
        abstracts and MeSH labels.
    '''
    list_cols = [
            'json_funding_project', 
            'terms_descriptive_project',
            'terms_mesh_abstract', 
            'terms_of_countryTags',
            ]
    key = 'world_report/wr_scanner_with_mesh.csv.bz2'
    df = pd.read_csv(
            smart_open(S3_PATH.format(key)),
            converters=eval_cols(list_cols), 
            chunksize=chunksize,
            compression='bz2')
    return df
