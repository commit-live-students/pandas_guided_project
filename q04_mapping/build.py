# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q04_mapping(path1, path2):
    df_02 = q01_load_data(path1)
    df_02.loc[len(df_02)] = df_02.iloc[:,6:10].sum(axis=0) 
    df_02.fillna(value=0, inplace=True, axis=0)
    
    df_03 = pd.read_csv(path2)   
    mapping = dict(zip(df_03['United States of America'].str.lower(), df_03['Unnamed: 6']))

    df_02.insert(loc=5, column='abbr', value='')
    df_02.iloc[:,6]=df_02['state'].map(mapping)
    
    return df_02 
    
q04_mapping(path1, path2)


