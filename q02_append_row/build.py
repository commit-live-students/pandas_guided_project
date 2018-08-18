# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path = 'data/excel-comp-data.xlsx'

def q02_append_row(path):
    df = q01_load_data(path)
    df.loc[len(df)] = df.iloc[:,6:10].sum(axis=0) 

    return df

q02_append_row(path)


