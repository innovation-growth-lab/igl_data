from igl_data.data.s3_transfer import load_df_pkl

bucket = 'igl-public'
folder = 'dap-innovation-tutorials/mag'

def mag_table(table='fields_of_study'):
    '''grid_table
    Get tables from the Microsoft Academic Graph database.

    Parameters
    ----------
    table : str
        Name of the Microsoft Academic Graph table to load. 
        Tables available include:
            - fields_of_study

    Returns
    -------
    DataFrame
        A dataframe with containing the Microsoft Academic Graph table data.
    '''
    key=f'{folder}/mag_{table}.pkl.bz2'
    return load_df_pkl(bucket, key)
