import ast
import smart_open
import pandas as pd

from igl_data.utilities import eval_cols 
from igl_data.data.s3_transfer import load_df_pkl

bucket = 'igl-public'
folder = 'dap-innovation-tutorials/gateway-to-research'

def gtr_sample():
    '''gateway_to_research_projects
    Get Gateway to Research projects csv and return as dataframe.
    '''
    bucket='igl-public'
    gtr_projects_key='dap-innovation-tutorials/gateway-to-research/gtr_projects.csv'
    list_cols = ['research_topics', 'research_subjects']
    gtr_projects_df = pd.read_csv(
        smart_open.smart_open("https://s3.us-east-2.amazonaws.com/{}/{}".format(bucket, gtr_projects_key)),
        converters=eval_cols(list_cols),
        index_col=0
    )
    return gtr_projects_df

def gtr_table(table):
    '''gtr_table
    Get a table from the Gateway to Research database.

    Parameters
    ----------
    table : str
        Name of the table to load. Tables available include:
            - funds
            - organisations
            - organisations_locations
            - outcomes_artisticandcreativeproducts
            - outcomes_collaborations
            - outcomes_disseminations
            - outcomes_furtherfundings
            - outcomes_impactsummaries
            - outcomes_intellectualproperties
            - outcomes_keyfindings
            - outcomes_policyinfluences
            - outcomes_products
            - outcomes_publications
            - outcomes_researchdatabaseandmodels
            - outcomes_researchmaterials
            - outcomes_softwareandtechnicalproducts
            - outcomes_spinouts
            - participant
            - persons
            - projects
            - topic
    Returns
    -------
    DataFrame
        A dataframe with containing the GtR table data.
    '''
    key=f'{folder}/gtr_{table}.pkl.bz2'
    return load_df_pkl(bucket, key)

def gtr_link_table(table):
    '''gtr_link_table
    Get a link table from the Gateway to Research database.
    Link tables link project ids to other entities within GtR.

    Parameters
    ----------
    table : str
        Name of the link table to load. Tables available include:
            - funds
            - organisations
            - organisations_locations
            - outcomes_artisticandcreativeproducts
            - outcomes_collaborations
            - outcomes_disseminations
            - outcomes_furtherfundings
            - outcomes_impactsummaries
            - outcomes_intellectualproperties
            - outcomes_keyfindings
            - outcomes_policyinfluences
            - outcomes_products
            - outcomes_publications
            - outcomes_researchdatabaseandmodels
            - outcomes_researchmaterials
            - outcomes_softwareandtechnicalproducts
            - outcomes_spinouts
            - participant
            - persons
            - topic
    Returns
    -------
    DataFrame
        A dataframe with containing the GtR table data.
    '''
    key=f'{folder}/link_tables/gtr_{table}_link.pkl.bz2'
    return load_df_pkl(bucket, key)

def gtr_table_list():
    d = [
            'funds',
            'organisations',
            'organisations_locations',
            'outcomes_artisticandcreativeproducts',
            'outcomes_collaborations',
            'outcomes_disseminations',
            'outcomes_furtherfundings',
            'outcomes_impactsummaries',
            'outcomes_intellectualproperties',
            'outcomes_keyfindings',
            'outcomes_policyinfluences',
            'outcomes_products',
            'outcomes_publications',
            'outcomes_researchdatabaseandmodels',
            'outcomes_researchmaterials',
            'outcomes_softwareandtechnicalproducts',
            'outcomes_spinouts',
            'participant',
            'persons',
            'projects',
            'topic',
        ]
    return d
