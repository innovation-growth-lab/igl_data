import ast
import smart_open
import pandas as pd

from igl_data.utilities import double_eval
from igl_data.data.s3_transfer import load_df_pkl

bucket = 'igl-public'
folder = 'dap-innovation-tutorials/arxiv'

def arxiv_table(table):
    '''arxiv_table
    Get a list of 
    Parameters
    ----------
    table : str
        Name of the ArXiv table to load. Tables available include:
            - article_categories
            - article_corex_topics
            - article_fields_of_study
            - article_institutes
            - categories
            - corex_topics
    Returns
    -------
    DataFrame
        A dataframe with containing the ArXiv table data.
    '''
    key=f'{folder}/arxiv_{table}.pkl.bz2'
    return load_df_pkl(bucket, key)

def arxiv_articles(chunk=None):
    '''arxiv_articles
    Get ArXiv article data chunks.

    Parameters
    ----------
    chunk : int
        Specify a particular chunk of data to download. There are 17
        chunks numbered 0 through 16.
    
    Returns
    -------
    generator
        A generator that returns ArXiv articles in chunks of 100,000
    
    or

    DataFrame
        A dataframe from a single chunk.
    '''
    if chunk is None:
        for i in range(16):
            key = f'{folder}/arxiv_articles_{i:02}.pkl.bz2'
            yield load_df_pkl(bucket, key)
    else:
        key = f'{folder}/arxiv_articles_{chunk:02}.pkl.bz2'
        return load_df_pkl(bucket, key)

def arxiv_sample_2017():
    '''arxiv_papers
    Get arXiv papers csv for a single year and return as dataframe.

    Args:
        year (`int`): Year of the dataset.
    Returns:
        arxiv_df (`pd.DataFrame`): Parsed dataframe of arXiv papers.
    '''
    year = 2017
    bucket='innovation-mapping-tutorials'
    key='arxiv_{}/arxiv_{}.csv'.format(year, year)
    arxiv_df = pd.read_csv(
        smart_open.smart_open('https://s3.us-east-2.amazonaws.com/{}/{}'.format(bucket, key)),
        index_col=0,
        converters={
            'authors': double_eval,
        },
        parse_dates=['created'],
    )
    arxiv_df['year_created'] = arxiv_df['created'].dt.year
    arxiv_df['category_ids'] = arxiv_df['category_ids'].str.split(',')
    return arxiv_df
