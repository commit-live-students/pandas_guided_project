# %load q05_replace_missing_values/build.py
import pandas as pd
import numpy as np
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
def q05_replace_missing_values(path1,path2):
    df = pd.read_excel(path1)
    df['total']=df['Jan']+df['Feb']+df['Mar']
    df.loc[len(df),:]=df.sum()
    df1 = pd.read_csv(path2)
    
    abbr_dict = dict(zip(df1.iloc[:,[1,6]]['United States of America'],df1.iloc[:,[1,6]]['Unnamed: 6']))
    
    df.iloc[:,6]  = df['state'].map(abbr_dict)
    df.iloc[6,6]  = 'MS'
    df.iloc[10,6] = 'TN'
    
    return df

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
q05_replace_missing_values(path1, path2)

#print(q05_replace_missing_values(path1,path2).shape)


