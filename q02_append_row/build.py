# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path = 'data/excel-comp-data.xlsx'

def q02_append_row(path):
    'write your solution here'

    df = q01_load_data(path)
    a =df['Jan'].sum()
    b = df['Feb'].sum()
    c = df['Mar'].sum()
    d = df['total'].sum()
    list_new = [[a,b,c,d]]
    df_final = df.append(pd.DataFrame(list_new,columns = ['Jan','Feb','Mar','total']))
    return df_final






