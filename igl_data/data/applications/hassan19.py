import smart_open
import pandas as pd
from typing import List, Union, Tuple

S3_PATH = 'https://s3.eu-west-2.amazonaws.com/igl-public/tutorials-data/applications/hassan19/{}'

types = {
    'date': str,
    'author': str,
    'title': str,
    'article': str,
    'section': str,
    'publication': str
}

cols = [
    'date',
    'author',
    'title', 'article',
    'section', 'publication'
]

def get_hassan_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load data from Hassan et al. (2019) paper.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: news, lexicon, risk
    """    
    with smart_open.open(S3_PATH.format(f"news.csv"), 'rb') as f:
        news = pd.read_csv(f, use_cols = cols, dtype = types)
    with smart_open.open(S3_PATH.format(f"NRC_lexicon.xlsx"), 'rb') as f:
        lexicon = pd.read_excel(f, engine="openpyxl")
    with smart_open.open(S3_PATH.format(f"risk_synonyms.xlsx"), 'rb') as f:
        risk = pd.read_excel(f, engine="openpyxl")
    return news, lexicon, risk