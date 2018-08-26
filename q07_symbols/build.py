# %load q07_symbols/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q06_sub_total.build import q06_sub_total

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q07_symbols(path1, path2):
    df1 = pd.read_excel(path1)
    df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
    df1.loc[len(df1),:]=df1.sum()
    df2 = pd.read_csv(path2)
    abbr_dict = dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2.iloc[:,[1,6]]['Unnamed: 6']))
    df1['abbr']=df1['state'].map(abbr_dict)
    #df1.drop(df1.columns[[6,7,]], axis=1,inplace=True)
    #df1.loc[df1[6,6].fillna('MS',inplace=True)
    list1 = ['MSS','TEN','none']
    df1['abbr']=df1['abbr'].fillna('MS',limit=1)
    df1['abbr']=df1['abbr'].fillna('TN',limit=1)
    df1['abbr']=df1['abbr'].fillna('None',limit=1)
    df1 = df1.drop(df1.index[len(df1)-1])
    df =df1.groupby('abbr')['Jan','Feb','Mar','total'].sum()
    df['total'] = df['total'].astype(int).apply(lambda x: '{:,}'.format(x)) 
    df=df.applymap(lambda x: '$'+ str(x))
    return df



q07_symbols(path1, path2)







