import ast
import smart_open

import pandas as pd

def sdg_web_articles():
    '''sdg_web_articles
    Get SDG web articles scraped from web and return as DataFrame.
    '''
    bucket='igl-public'
    gtr_projects_key='dap-innovation-tutorials/sdg/sdg_web_articles.json'
    list_cols = ['sdg_goals']
    gtr_projects_df = pd.read_json(
        smart_open.open("https://s3.us-east-2.amazonaws.com/{}/{}".format(bucket, gtr_projects_key)),
    )
    return gtr_projects_df
