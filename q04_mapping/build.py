# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
from greyatomlib.pandas_guided_project.q03_scrape_clean.build import q03_scrape_clean
def q04_mapping(path1,path2):
    "write your solution here"
    df1 = q02_append_row(path1)
    df2 = q03_scrape_clean(path2)
    return df1,df2



path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
q04_mapping(path1,path2)
