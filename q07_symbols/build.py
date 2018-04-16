import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q06_sub_total.build import q06_sub_total

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q07_symbols(path1,path2):
    "write your solution here"
    df_sub = q06_sub_total(path1,path2)
    formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))
    return formatted_df
