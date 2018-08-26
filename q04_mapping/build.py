# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
from greyatomlib.pandas_guided_project.q03_scrape_clean.build import q03_scrape_clean


path1 = './data/excel-comp-data.xlsx'
path2 = './data/scraped.csv'

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





