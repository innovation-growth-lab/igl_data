import smart_open
import pandas as pd
import pickle

from igl_data.data.s3_transfer import load_df_pkl


bucket='igl-public'

def patents_10k():
    '''patents_10k
    Gets a pre-selected sample of 10,000 patents from ONS.
    '''
    patents_10k_key='dap-innovation-tutorials/ons/ONS_y02_sample_10000.pkl.bz2'
    return load_df_pkl(bucket, patents_10k_key)

def patents_100k():
    '''patents_100k
    Gets a pre-selected sample of 100,000 patents from ONS.
    '''
    patents_100k_key='dap-innovation-tutorials/ons/ONS_y02_sample_100000.pkl.bz2'
    return load_df_pkl(bucket, patents_100k_key)
