import ast
import pandas as pd
import numpy as np
from smart_open import smart_open

S3_PATH = 'https://s3.us-east-2.amazonaws.com/igl-public/dap-innovation-tutorials/{}'

def country_basic_info():
    '''country_basic_info
    Country level data from RestCountries API.

    Fields:
       'alpha2Code', 'alpha3Code', 'altSpellings', 'area', 'borders',
       'callingCodes', 'capital', 'cioc', 'currencies', 'demonym', 'flag',
       'gini', 'languages', 'latlng', 'name', 'nativeName', 'numericCode',
       'population', 'region', 'regionalBlocs', 'subregion', 'timezones',
       'topLevelDomain', 'translations' 
    '''
    key = 'gis/countries_basic.csv'
    eval_cols = [
            'altSpellings', 'altSpellings', 'callingCodes', 'currencies',
            'regionalBlocs', 'timezones', 'translations', 'latlng', 'languages',
            'borders', 
            ]
    df = pd.read_csv(
            smart_open(S3_PATH.format(key)),
            converters={k: ast.literal_eval for k in eval_cols}
            )
    df['lat'] = [l[0] if len(l) == 2 else np.nan for l in df['latlng']]
    df['lng'] = [l[1] if len(l) == 2 else np.nan for l in df['latlng']]
    return df
    
