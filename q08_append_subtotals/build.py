# %load q08_append_subtotals/build.py
import pandas as pd
import numpy as np
import sys,os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q06_sub_total.build import q06_sub_total
#from greyatomlib.pandas_guided_project.q07_symbols.build import q07_symbols
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q08_append_subtotals(path1,path2):
    'write your solution here'
    df_02 = q01_load_data(path1)
    df_02.loc[len(df_02)] = df_02.iloc[:,6:10].sum(axis=0) 
    df_02.fillna(value=0, inplace=True, axis=0)
    df_03 = pd.read_csv(path2)   
    mapping = dict(zip(df_03['United States of America'].str.lower(), df_03['Unnamed: 6']))
    df_02.insert(loc=6, column='abbr', value='')
    df_02.iloc[:,6]=df_02['state'].map(mapping)
    df_02.iloc[6,6] = 'MS'
    df_02.iloc[10,6] = 'TN'
    
    df_sub = df_02.groupby(['abbr'])[['Jan', 'Feb', 'Mar', 'total']].sum()
    df_sub.loc[len(df_sub)] = df_sub.iloc[:].sum(axis=0)
    
    df_sub = df_sub.applymap(lambda x: '$%s'% '{:,}'.format(int(x)))
    return df_sub
    
q08_append_subtotals(path1,path2)



