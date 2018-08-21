# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
def q04_mapping(path1,path2):
    'write your solution here'
    
    df1 = q02_append_row(path1)
    df1['abbr'] = np.nan
    df2 = pd.read_csv(path2)
    ab = df2.iloc[:,7]
    name = df2['United States of America']
    d = {}
    for i in range(0,ab.shape[0]):
        d[name[i].lower()] = ab[i]

    for i in range(0,df1.shape[0]):
        if df1.iloc[i,:]['state'] in d.keys():
            df1.iloc[i,-1] = d[df1.iloc[i,:]['state']]

    df2 = df1.iloc[:,0:5]
    df2['total'] = df1['total']
    df2['abbr'] = df1['abbr']
    return df2


q04_mapping(path1, path2)

