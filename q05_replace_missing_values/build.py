# %load q05_replace_missing_values/build.py
import pandas as pd
import numpy as np
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
from greyatomlib.pandas_guided_project.q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
def q05_replace_missing_values(path1,path2):

    df_02 = q01_load_data(path1)
    df_02.loc[len(df_02)] = df_02.iloc[:,6:10].sum(axis=0) 
    df_02.fillna(value=0, inplace=True, axis=0)
    
    df_03 = pd.read_csv(path2)   
    mapping = dict(zip(df_03['United States of America'].str.lower(), df_03['Unnamed: 6']))

    df_02.insert(loc=6, column='abbr', value='')
    df_02.iloc[:,6]=df_02['state'].map(mapping)
    
    #df_02 = q04_mapping (path1, path2)
    df_02.iloc[6,6] = 'MS'
    df_02.iloc[10,6] = 'TN'
    
    return df_02 

print(q05_replace_missing_values(path1,path2).shape)


