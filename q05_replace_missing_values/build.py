# %load q05_replace_missing_values/build.py
import pandas as pd
import numpy as np
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
# def q05_replace_missing_values(path1,path2):
def q01_load_data(path):
    data = pd.read_excel(path)

    data['state'] = data.state.str.lower()
    data['total'] = data[['Jan','Feb','Mar']].sum(axis=1)

    return data

def q02_append_row(path):

    df = q01_load_data(path)
    sum_row = df[['Jan', 'Feb', 'Mar', 'total']].sum()
    df_sum = pd.DataFrame(data=sum_row).T
    df_final = df.append(df_sum,ignore_index = True)
    return df_final
def q04_mapping(path1,path2):
    
    a = pd.read_excel(path1)
    b = pd.read_csv(path2)
    b['United States of America'] = b['United States of America'].astype(str).str.lower()
    b['US'] = b['US'].astype(str)
    mapping = b.set_index('United States of America').to_dict()['US']
    mapping['mississipi']=mapping.pop('mississippi')
    mapping['tenessee']=mapping.pop('tennessee')
    new_df = q02_append_row(path1)
#   new['abbr'] = np.nan
    new_df.insert(loc = 6,column = 'abbr', value = np.nan)
    new_df['state'] = new_df['state'].map(mapping)
    return new_df
def q05_replace_missing_values(path1,path2):
    df_replace = q04_mapping(path1,path2)
    df_mississippi = pd.DataFrame(df_replace.iloc[6,:]).T
    df_tenessee = pd.DataFrame(df_replace.iloc[10,:]).T
    df_tenessee = df_tenessee.replace(np.nan,'TN')
    df_mississippi = df_mississippi.replace(np.nan,'MS')
    df_replace.iloc[6,6] = 'MS'
    df_replace.iloc[10,6] = 'TN'
    return df_replace

q05_replace_missing_values(path1,path2)
#print(q05_replace_missing_values(path1,path2).shape)


