import pandas as pd
import smart_open
import ast

from igl_data.data.s3_transfer import load_df_pkl


bucket = 'igl-public'
folder = 'dap-innovation-tutorials/cordis/mysql'
S3_PATH = 'https://s3.us-east-2.amazonaws.com/igl-public/dap-innovation-tutorials/{}'

def cordis_table(table):
    '''cordis_table
    Get a table from the CORDIS database.

    Parameters
    ----------
    table : str
        Name of the table to load. Tables available include:
            - organisations
            - project_organisations
            - project_proposal_calls
            - project_topics
            - projects
            - proposal_calls
            - publications
            - reports
            - topics

    Returns
    -------
    DataFrame
        A dataframe with containing the CORDIS table data.
    '''
    key=f'{folder}/cordis_{table}.pkl.bz2'
    return load_df_pkl(bucket, key)

def cordis_table_list():
    d = [
        'organisations',
        'project_organisations',
        'project_proposal_calls',
        'project_topics',
        'projects',
        'proposal_calls',
        'publications',
        'reports',
        'topics',
        ]
    return d

def _projects_h2020_fp6(key):
    file_path = S3_PATH.format(key)
    df = pd.read_csv(
        smart_open.open(file_path),
        sep=';',
        encoding='iso-8859-1',
        parse_dates=['startDate', 'endDate'],
        infer_datetime_format=True,
        decimal=','
    )
    df['organisations'] = (df['coordinator'] + ';' +  df['participants']).fillna(df['coordinator'])
    df['countries'] = (df['coordinatorCountry'] + ';' +  df['participantCountries']).fillna(df['coordinatorCountry'])
    list_cols = ['organisations', 'countries', 'participants', 'participantCountries', 'programme']
    for col in list_cols:
        df[col] = df[col].str.split(';')

    df['startYear'] = df['startDate'].dt.year
    df['endYear'] = df['endDate'].dt.year
    return df

def h2020_projects():
    key = 'cordis/h2020/cordis-h2020projects.csv'
    return _projects_h2020_fp6(key)