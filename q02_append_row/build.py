# %load q02_append_row/build.py
import pandas as pd
import sys, os
from pandas import ExcelWriter
from pandas import ExcelFile

path = 'data/excel-comp-data.xlsx'

#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

def q02_append_row(path):
    # 'write your solution here'
    df = pd.read_excel(path)
    df['total'] = df['Jan']+df['Feb']+df['Mar']  
    # print (df)
    
    df2 = pd.DataFrame(columns = df.columns)

    t1 = df['Jan'].sum()
    t2 = df['Feb'].sum()
    t3 = df['Mar'].sum()
    t4 = df['total'].sum()

    df2.loc[0,'Jan'] = t1
    df2.loc[0,'Feb'] = t2
    df2.loc[0,'Mar'] = t3
    df2.loc[0,'total'] = t4
    
    df=df.append(df2)
    return df

#q02_append_row(path)






