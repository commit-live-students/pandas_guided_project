# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
df= q01_load_data(path='data/excel-comp-data.xlsx')

def q02_append_row(path='data/excel-comp-data.xlsx'):
    a=df.append(df[['Jan','Feb','Mar','total']].sum(),ignore_index=True)
    return a
#     a=df.append([df[['Jan','Feb','Mar']].sum()],ignore_index=True)<--This is how you create a new row in a dataframe
    
   





c=q02_append_row(path='data/excel-comp-data.xlsx')
c




