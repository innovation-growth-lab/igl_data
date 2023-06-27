from igl_data.data.s3_transfer import load_df_pkl

bucket = 'igl-public'
folder = 'dap-innovation-tutorials/grid'

def grid_table(table):
    '''grid_table
    Get tables from the GRID database.

    Parameters
    ----------
    table : str
        Name of the GRID table to load. Tables available include:
            - aliases
            - institutes

    Returns
    -------
    DataFrame
        A dataframe with containing the GRID table data.
    '''
    key=f'{folder}/grid_{table}.pkl.bz2'
    return load_df_pkl(bucket, key)
