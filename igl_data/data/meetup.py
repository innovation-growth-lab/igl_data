import ast
import pandas as pd
from smart_open import smart_open

S3_PATH = 'https://s3.eu-west-2.amazonaws.com/igl-public/dap-innovation-tutorials/{}'

def _parse_meetup_topics(topic_list):
    names = []
    for t in topic_list:
        names.append(t.get('name'))
    names = [name for name in names if name is not None]
    return names

def meetups(country='europe'):
    '''meetups
    Meetup group information.

    Fields:
        'category', 'category_id', 'category_name', 'category_shortname',
        'city', 'country', 'country_code', 'country_name', 'created',
        'created_at', 'db', 'description', 'group_name', 'id', 'lang', 'lat',
        'lon', 'members', 'name', 'timestamp', 'topics', 'urlkey', 'urlname',
        'year', 'topic_names'
    '''
    list_cols = ['name', 'urlkey']
    key = 'meetup/meetups_{}.csv'.format(country)
    df = pd.read_csv(
            smart_open(S3_PATH.format(key)),
            converters={'topics': ast.literal_eval}
            )
    for col in list_cols:
        df[col] = df[col].str.split(',')
    return df
