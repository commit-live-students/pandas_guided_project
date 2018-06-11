# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path = 'data/excel-comp-data.xlsx'

def q02_append_row(path):
    df=q01_load_data(path)
    col_list=['Jan','Feb','Mar','total']
    df_inter= df[col_list].sum(axis=0).to_frame().T
    df_final=pd.concat([df,df_inter])
    return df_final
    


    
#print(q02_append_row(path))
    






