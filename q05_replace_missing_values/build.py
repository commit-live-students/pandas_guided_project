# %load q05_replace_missing_values/build.py
import pandas as pd
import numpy as np
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
def q05_replace_missing_values(path1,path2):
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
        return df1
        
#         mapping={}
#         for i,j in zip(df2['United States of America'],df2['US']):
#             mapping[i]=j

#         state=[]
#         for i in (df1['state']):
#             state.append(i)

#         f=[]
#         # for i,j in mapping.items():
#         #     for k in state:
#         #         print(k)
# #         del state[15]
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
#         df1.insert(loc=6,column='abbr',value=g)
#         return df1
        


c=q05_replace_missing_values(path1,path2)
c


