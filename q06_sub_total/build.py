# %load q06_sub_total/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q05_replace_missing_values.build import q05_replace_missing_values
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q06_sub_total(path1,path2):
    'write your solution here'
    df_02 = q01_load_data(path1)
    df_02.loc[len(df_02)] = df_02.iloc[:,6:10].sum(axis=0) 
    df_02.fillna(value=0, inplace=True, axis=0)
    
    df_03 = pd.read_csv(path2)   
    mapping = dict(zip(df_03['United States of America'].str.lower(), df_03['Unnamed: 6']))
    df_02.insert(loc=5, column='abbr', value='')
    df_02.iloc[:,6]=df_02['state'].map(mapping)
    
    df_02.iloc[6,6] = 'MS'
    df_02.iloc[10,6] = 'TN'
    
    #df_02 = q05_replace_missing_values(path1,path2)
    df_sub = df_02.groupby(['postal-code'])[['account', 'Jan', 'Feb', 'Mar']].sum()
    return df_sub

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
q06_sub_total(path1, path2)



