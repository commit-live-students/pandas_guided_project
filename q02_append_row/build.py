# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path = './data/excel-comp-data.xlsx'
def q02_append_row(path):
    data_set = q01_load_data(path)
    '''
    Approach 1
    '''
    data_set.at['Grand Total', 'Jan'] = data_set['Jan'].sum()
    data_set.at['Grand Total', 'Feb'] = data_set['Feb'].sum()
    data_set.at['Grand Total', 'Mar'] = data_set['Mar'].sum()
    data_set.at['Grand Total', 'total'] = data_set['total'].sum()
    
    return data_set
q02_append_row(path)





