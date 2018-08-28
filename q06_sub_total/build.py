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

# def q06_sub_total(path1,path2):
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
    'write your solution here'
    df_final = q04_mapping(path1,path2)
    df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')
    df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')
    df_final.replace(df_final.iloc[6], df_mississipi, inplace=True)
    df_final.replace(df_final.iloc[10], df_tenessee, inplace=True)
    return df_final

def q06_sub_total(path1,path2):
    group  = q05_replace_missing_values(path1,path2)
    df_sub = group[['state', 'Jan', 'Feb', 'Mar', 'total']].groupby('state').sum()
    return df_sub

q06_sub_total(path1,path2)



