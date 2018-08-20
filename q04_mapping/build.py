# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row

#Custom
from greyatomlib.pandas_guided_project.q03_scrape_clean.build import q03_scrape_clean

def q04_mapping(path1,path2):
    df_from_appended_row = q02_append_row(path1)
    df_from_scraped_data = q03_scrape_clean(path2)

    #Approach 1 for creating a dictionary
    mapping = df_from_scraped_data.set_index('United States of America').to_dict()['U.S.']    
    mapping = {k.lower(): v for k,v in mapping.items()}
    df_final = df_from_appended_row

    #Inseting 'abbr' at column 6 - Approach 2 for this is given below
    df_final.insert(6, 'abbr', '')
    df_final['abbr'] = df_final['state'].map(mapping)

    return df_final

path1 = 'data/excel-comp-data.xlsx'
path2 = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
q04_mapping(path1, path2)


