# %load q06_sub_total/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q05_replace_missing_values.build import q05_replace_missing_values


def q04_mapping(path1,path2):
    'write your solution here'
    df = pd.read_csv(path2)
    namesList =  df['United States of America'].values
    abbrList = df['US'].values
    zippedList = list(zip(namesList, abbrList))
    mapping = dict(zippedList)
    
    df = pd.read_excel(path1)
    abbr = list()
    for state in df['state'].values:
        if state in mapping.keys() : abbr.append(mapping[state])
        else : abbr.append(np.nan)
    pd.Series(abbr)
    
    df.insert(6, 'abbr', abbr)
    return df

def q05_replace_missing_values(path1,path2):
    df = q04_mapping(path1, path2)
    df.at[6, 'abbr'] = 'MS'
    df.at[10, 'abbr'] = 'TN'
    return df

def q06_sub_total(path1,path2):
    'write your solution here'
    df = q05_replace_missing_values(path1, path2)
    df = df.groupby(['abbr']).sum()
    df = df[['account', 'Jan', 'Feb', 'Mar']]
    return df



