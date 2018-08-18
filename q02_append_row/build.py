# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

def q02_append_row(path):
    #'write your solution here'
    df_final =q01_load_data(path)
    sum_row=df_final[['Jan','Feb','Mar','total']].sum()
    df_sum=pd.DataFrame(data=sum_row).T
    df_sum=df_sum.reindex(columns=df_final.columns)
    df=df_final.append(df_sum,ignore_index=True)
    #df_final.sum(numeric_only=True)
    #df_final.append(df_final.sum(numeric_only=True).T, ignore_index=True)
    return  df





