import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
def q05_replace_missing_values(path1,path2):
    'write your solution here'
    df_final = q04_mapping(path1,path2)
    df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')
    df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')
    df_final.replace(df_final.iloc[6], df_mississipi, inplace=True)
    df_final.replace(df_final.iloc[10], df_tenessee, inplace=True)
    return df_final



