# %load q06_sub_total/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q05_replace_missing_values.build import q05_replace_missing_values

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q06_sub_total(path1,path2):
        df1=pd.read_excel(path1)
        df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
        df1.loc[len(df1),:]=df1.sum()
        df2=pd.read_csv(path2)
        abbr_dict=dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2['US']))#
        f=list(df1['state'])
        for i,j in enumerate(f):
            if j=='Northcarolina':
                f[i]='NorthCarolina'
            elif j=='Mississipi':
                f[i]='Mississippi'
            elif j=='Rhodeisland':
                f[i]='RhodeIsland'
            elif j=='Tenessee':
                f[i]='Tennessee'
            elif j=='Northdakota':
                f[i]='NorthDakota'
        df1['state']=f
        dftemp=df1['state'].map(abbr_dict)
        df1.insert(loc=6,column='abbr',value=dftemp)
        groupby_abbr_sum=df1.groupby('abbr')[['Jan','Feb','Mar','total']].sum()
        return groupby_abbr_sum



c=q06_sub_total(path1,path2)
c


