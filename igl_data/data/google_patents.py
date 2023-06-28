import smart_open
import pandas as pd
from typing import List, Union

S3_PATH = 'https://s3.eu-west-2.amazonaws.com/igl-public/tutorials-data/patents/{}'

def list_countries() -> List[str]:
    return [
        "AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "GB", "GR", "HR",
        "HU", "IE", "IS", "IT", "LT", "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI",
        "SK"
    ]


def google_patents(country: Union[str, List[str]] = "GB"):
    """Load parquet files as pandas dataframes, append any subset of 2 ISO name country files
        one per country. EU.

    Args:
        country (Union[str, None], optional): List of countries to load. Defaults to "GB".
    """

    if isinstance(country, str):
        with smart_open.open(S3_PATH.format(f"patents_clean_{country}.parquet"), 'rb') as f:
            return pd.read_parquet(f)
    
    elif isinstance(country, list):
        dfs = []
        for c in country:
            with smart_open.open(S3_PATH.format(f"patents_clean_{c}.parquet"), 'rb') as f:
                dfs.append(pd.read_parquet(f))
        return pd.concat(dfs)
