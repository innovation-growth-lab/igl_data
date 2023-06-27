import ast
import itertools
import numpy as np

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def print_counter_most_common(counter, n, name='Item', padding=30, stats=True):
    print('{}\tFrequency'.format(name))
    for item, count in counter.most_common(n):
            print('{}\t{}'.format(item, count))

    if stats:
        vals = counter.values()
        lo = np.percentile(vals, 25)
        med = np.median(vals)
        up = np.percentile(vals, 75)
        print('\nLower Quartile: {}'.format(lo))
        print('Median:           {}'.format(med))
        print('Upper Quartile:   {}'.format(up))
        # print('Upper Quartile:   {}')

def flatten_lists(l):
    '''flatten_lists
    Unpacks nested lists into one list of elements.
    '''
    return list(itertools.chain(*l))

def eval_cols(cols):
    '''eval_cols
    Returns a dictionary to convert columns with ast.literal_eval when reading
    a csv with pandas.

    Args:
        cols (`list` of `str`): List of column names

    Returns:
        (`dict`): Dict of column name keys and ast.literal eval as values
    '''
    return {col: ast.literal_eval for col in cols}

def double_eval(x):
    return ast.literal_eval(ast.literal_eval(x))

