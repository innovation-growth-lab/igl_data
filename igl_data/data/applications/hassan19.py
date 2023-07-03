import smart_open
import pandas as pd
from typing import List, Union

S3_PATH = 'https://s3.eu-west-2.amazonaws.com/igl-public/tutorials-data/applications/hassan19/{}'

def get_hassan_data():
    with smart_open.open(S3_PATH.format(f"news.csv"), 'rb') as f:
        news = pd.read_csv(f)
    with smart_open.open(S3_PATH.format(f"NRC_lexicon.xlsx"), 'rb') as f:
        lexicon = pd.read_excel(f, engine="openpyxl")
    with smart_open.open(S3_PATH.format(f"risk_synonyms.xlsx"), 'rb') as f:
        risk = pd.read_excel(f, engine="openpyxl")
    return news, lexicon, risk