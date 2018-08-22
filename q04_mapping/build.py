# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
from greyatomlib.pandas_guided_project.q03_scrape_clean.build import q03_scrape_clean
df= q01_load_data(path='data/excel-comp-data.xlsx')
a=df.append(df[['Jan','Feb','Mar','total']].sum(),ignore_index=True)
a
b=q03_scrape_clean(url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations' )
b.reset_index(drop=True)
def q04_mapping(path1='data/excel-comp-data.xlsx',path2='data/scraped.csv'):
#         mapping={}
#         for i,j in zip(b['United States of America'],b['US']):
#             mapping[i]=j

#         state=[]
#         for i in (a['state']):
#             state.append(i)

#         f=[]
#         # for i,j in mapping.items():
#         #     for k in state:
#         #         print(k)
#         del state[15]
#         for i in state:
#             f.append(i.capitalize())

#         for i,j in enumerate(f):
#             if j=='Northcarolina':
#                 f[i]='NorthCarolina'
#             elif j=='Mississipi':
#                 f[i]='Mississippi'
#             elif j=='Rhodeisland':
#                 f[i]='RhodeIsland'
#             elif j=='Tenessee':
#                 f[i]='Tennessee'
#             elif j=='Northdakota':
#                 f[i]='NorthDakota'
#         g=[]
#         for j in f:
#             for i in mapping.items():
#                 if j==i[0]:
#                     g.append(i[1])
#         g.append('NaN')
#         a.insert(loc=6,column='abbr',value=g)
#         return a
    df1=pd.read_excel(path1)
    df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
    df1.loc[len(df1),:]=df1.sum()
    df2=pd.read_csv(path2)
    abbr_dict=dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2['US']))
    dftemp=df1['state'].map(abbr_dict)
    df1.insert(loc=6,column='abbr',value=dftemp)
    return df1






c=q04_mapping(path1='data/excel-comp-data.xlsx',path2='data/scraped.csv')
c






