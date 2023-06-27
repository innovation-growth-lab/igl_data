# ArXiv

Tables available from arXiv data.

- [Papers Sample](#arXiv-Papers-Sample)
- [Articles](#arXiv-Articles)
- [Article Categories](#arXiv-Article-Categories)
- [Article CorEx Topics](#arXiv-Article-CorEx-Topics)
- [Article Fields of Study](#arXiv-Article-Fields-of-Study)
- [Article Institutes](#arXiv-Article-Institutes)
- [Categories](#arXiv-Categories)
- [CorEX Topics](#arXiv-CorEx-Topics)

### arXiv Papers Sample

A sample dataset of 2017 papers from arXiv including the abstract and some metadata.

```python
from igl_data.data.arxiv import arxiv_sample_2017
arxiv_papers_df = arxiv_sample_2017()
```

- **`id`**
- **`title`**
- **`authors`**
- **`doi`**
- **`created`**
- **`abstract`**
- **`category_ids`**
- **`year_created`**

### arXiv Articles

Articles from arXiv including the title, abstract and metadata. There are 1.7 million articles, which can be loaded in chunks of 100,000 at a time.

```python
from igl_data.data.arxiv import arxiv_articles
arxiv_articles = arxiv_articles()

for a in arxiv_articles:
    ...
```

- **`id`** (`str`): ArXiv article ID.
- **`datestamp`**
- **`created`**
- **`updated`**
- **`title`** (`str`):
- **`journal_ref`** (`str`):
- **`doi`** (`str`):
- **`abstract`** (`str`):
- **`authors`** (`list of json`): Author list from arXiv.
- **`mag_authors`**  (`str`): Author list from Microsoft Academic Graph.
- **`mag_id`** (`list`): Microsoft Academic Graph ID.
- **`mag_match_prob`** (`float`): How well the title was matched to an article in Microsoft Academic Graph.
- **`citation_count`** (`int`): Number of citations at `citation_count_updated`.
- **`citation_count_updated`** (`datetime`): Date when citation count was last updated.
- **`msc_class`** (`str`):
- **`institute_match_attempted`** (`int`):

### arXiv Article Categories

Official arXiv categories matched to article IDs.

```python
from igl_data.data.arxiv import arxiv_table
arxiv_article_categories = arxiv_table('article_categories')
```

- **`article_id`** (`str`): Article ID.
- **`category_id`** (`str`): An arXiv category ID, e.g. 'hep-phys' (high energy particle physics)

### arXiv Article CorEx Topics

A set of topic modelled topics from machine learning and AI arXiv papers. Matches one or more of 27 topics to articles via their IDs along with a weight, denoting the importance of the topic for an article.

```python
from igl_data.data.arxiv import arxiv_table
arxiv_article_categories = arxiv_table('article_corex_topics')
```

- **`article_id`** (`str`): Article ID.
- **`topic_id`** (`str`): ID of a topic from the `arxiv_corex_topics` table.
- **`weight`** (`float`): Importance of the topic for the article.

### arXiv Article Fields of Study

Maps Microsoft Academic Graph fields of study to arXiv paper IDs.

```python
from igl_data.data.arxiv import arxiv_table
arxiv_article_categories = arxiv_table('article_fields_of_study')
```

- **`article_id`** (`str`): Article ID.
- **`fos_id`** (`str`): Microsoft Academic Graph field of study ID.

### arXiv Article Institutes

Maps GRID institute IDs to arXiv paper IDs.

```python
from igl_data.data.arxiv import arxiv_table
arxiv_article_categories = arxiv_table('article_institutes')
```

- **`article_id`** (`str`): Article ID.
- **`institute_id`** (`str`): GRID institute ID.
- **`is_multinational`** (`int`): 1 if the institute is multi-national.
- **`matching_score`** (`float`): Between 0 and 1, denoting how well the institute name was matched to GRID.

### arXiv Categories

Maps arXiv category IDs to their descriptions.

```python
from igl_data.data.arxiv import arxiv_table
arxiv_article_categories = arxiv_table('categories')
```

- **`id`** (`str`): Category ID. e.g. *astro-ph*
- **`description`** (`str`): Category description. e.g. *Astrophysics*

### CorEx Topics

Maps 27 machine learning and AI topic IDs to the topic terms.

```python
from igl_data.data.arxiv import arxiv_table
arxiv_article_categories = arxiv_table('corex_topics')
```

- **`id`** (`int`): Topic ID.
- **`description`** (`list`): Topic terms.
