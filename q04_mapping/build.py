import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q04_mapping(path1,path2):
    'write your solution here'
    df1 = pd.read_excel(path1)
    df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
    df1.loc[len(df1),:]=df1.sum()
    
    df2 = pd.read_csv(path2)
    
    abbr_dict = dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2.iloc[:,[1,6]]['Unnamed: 6']))
    
    df1['abbr']=df1['state'].map(abbr_dict)
    df1.drop(df1.columns[[6,7,8,9]], axis=1,inplace=True) 
    #print (df1)
    return df1

q04_mapping(path1,path2)



