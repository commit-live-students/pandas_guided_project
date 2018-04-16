import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q05_replace_missing_values.build import q05_replace_missing_values

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q06_sub_total(path1,path2):
    'write your solution here'
    df_final = q05_replace_missing_values(path1,path2)
    #df_final['abbr'] = df_final['abbr'].astype(str)
    df_sub=df_final[['abbr', 'Jan', 'Feb', 'Mar', 'total']].groupby('abbr').sum()

    return df_sub


