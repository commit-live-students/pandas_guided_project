# %load q08_append_subtotals/build.py
import pandas as pd
import numpy as np
import sys,os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q06_sub_total.build import q06_sub_total
#from greyatomlib.pandas_guided_project.q07_symbols.build import q07_symbols


path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q08_append_subtotals(path1,path2):
    df1 = pd.read_excel(path1)
    df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
    df1.loc[len(df1),:]=df1.sum()
    df2 = pd.read_csv(path2)
    abbr_dict = dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2.iloc[:,[1,6]]['Unnamed: 6']))
    df1['abbr']=df1['state'].map(abbr_dict)
    df1['abbr']=df1['abbr'].fillna('MS',limit=1)
    df1['abbr']=df1['abbr'].fillna('TN',limit=1)
    df1['abbr']=df1['abbr'].fillna('None',limit=1)
    df1 = df1.drop(df1.index[len(df1)-1])
    df =df1.groupby('abbr')['Jan','Feb','Mar','total'].sum()
    
    
    t1 = pd.DataFrame(df['Jan']).sum()
    t2 = pd.DataFrame(df['Feb']).sum()
    t3 = pd.DataFrame(df['Mar']).sum()
    t4 = pd.DataFrame(df['total']).sum()
    Total = [t1,t2,t3,t4]
    df2 = pd.DataFrame(columns=df.columns)
    df2.loc[0] = df2['Jan'].append(Total)
    df_final = pd.concat([df, df2])
    df_final['total'] = df_final['total'].astype(int).apply(lambda x: '{:,}'.format(x))
    df_final['Jan'] = df_final['Jan'].astype(int).apply(lambda x: '{:,}'.format(x)) 
    df_final['Feb'] = df_final['Feb'].astype(int).apply(lambda x: '{:,}'.format(x)) 
    df_final['Mar'] = df_final['Mar'].astype(int).apply(lambda x: '{:,}'.format(x)) 
    df_final=df_final.applymap(lambda x: '$'+ str(x))
    df_final=df_final.rename(index={0: 'Total'})
    return df_final

q08_append_subtotals(path1,path2)




