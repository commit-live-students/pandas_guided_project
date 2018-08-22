# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path = 'data/excel-comp-data.xlsx'


def q02_append_row(path):
    df = pd.read_excel(path)
    df['total']=df['Jan']+df['Feb']+df['Mar']
    #df.loc[len(df),:]=None
    #df.loc[len(df),['Jan']]=df['Jan'].sum()
    #df.loc[len(df),['Feb']]=df['Feb'].sum()
    #df.loc[len(df),['Mar']]=df['Mar'].sum()
    #df.loc[len(df),['total']]=df['total'].sum()
    df.loc[len(df),:]=df.sum()
    return df
q02_append_row('data/excel-comp-data.xlsx')






