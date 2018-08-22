# %load q10_total/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q06_sub_total.build import q06_sub_total
import matplotlib.pyplot as plt
plt.switch_backend('agg')
path1='data/excel-comp-data.xlsx'
path2='data/scraped.csv'
def q10_total(path1,path2):

    'write your solution here'
    df1 = pd.read_excel(path1)
    df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
    df1.loc[len(df1),:]=df1.sum()
    df2 = pd.read_csv(path2)
    abbr_dict = dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2.iloc[:,[1,6]]['Unnamed: 6']))
    dftemp=df1['state'].map(abbr_dict)
    df1.insert(loc=6,column='abbr',value=dftemp)
    df1.iloc[6,6] = 'MS'
    df1.iloc[10,6] = 'TN'
    df3 = df1.groupby(['abbr']).sum()
    return df3.plot.pie(y='Jan',figsize=(8,8))
q10_total(path1,path2)


