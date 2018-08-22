# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
def q04_mapping(path1,path2):
    'write your solution here'
    df = pd.read_excel(path1)
    df['total']=df['Jan']+df['Feb']+df['Mar']
    df.loc[len(df),:]=df.sum()
    
    df1 = pd.read_csv(path2)
    
    abbr_dict = dict(zip(df1.iloc[:,[1,6]]['United States of America'],df1.iloc[:,[1,6]]['Unnamed: 6']))
    
    df.iloc[:,6]=df['state'].map(abbr_dict)
    
    return df

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
q04_mapping(path1, path2)



