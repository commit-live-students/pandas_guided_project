# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
path= 'data/excel-comp-data.xlsx'

def q02_append_row(path):
    'write your solution here'
    df=pd.read_excel(path)
    df['total'] = df['Jan']+df['Feb']+df['Mar']
    df.loc[len(df),:]= df.sum()
    print(df.head)
    return(df)
    
    





print(q02_append_row(path))




