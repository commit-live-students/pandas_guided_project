# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row, q01_load_data
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q04_mapping(path1,path2):
    'write your solution here'
    df_final= q02_append_row(path1)
    scraped = pd.read_csv(path2)
    print(df_final.head())
    print(scraped.head())
    scraped['United States of America'] = scraped['United States of America'].astype(str).apply(lambda x: x.lower())
    scraped['US'] = scraped['US'].astype(str)
    mapping = scraped.set_index('United States of America')['US'].to_dict()
    df_final.insert(6, 'abbr', np.nan)
    df_final['abbr'] = df_final['state'].map(mapping)
    return df_final


q04_mapping(path1,path2)
# Df=pd.read_excel(path1)
# print(Df.head(5))

q04_mapping(path1,path2)


