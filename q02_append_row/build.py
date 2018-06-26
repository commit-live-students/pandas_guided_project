#%load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path='data/excel-comp-data.xlsx'


def q02_append_row(path):
    df=q01_load_data(path)
    df_row=pd.DataFrame(df[['Jan','Feb','Mar','total']].sum()).T
    df_final=df.append(df_row,ignore_index=True)
    return df_final


