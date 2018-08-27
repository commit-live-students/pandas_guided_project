# %load q05_replace_missing_values/build.py
import pandas as pd
import numpy as np
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q04_mapping(path1,path2):
    df_scrap =pd.read_csv(path2)
    df_clean = pd.read_excel(path1)
    mapping = pd.Series(df_scrap['US'].values,index=df_scrap['United States of America']).to_dict()
    #df_clean.insert(loc=6, column='abbr' ,value ='nan')
    df_clean['abbr'] =  df_clean['state'].map(mapping)
    df_clean = df_clean[['account','name','street','city','state','postal-code','abbr','Jan','Feb','Mar']]
    return df_clean

def update_vals(row):
    if str(row.state) == 'Mississipi' and str(row.abbr) == 'nan':
        row.abbr  = 'MS'
    elif  str(row.state) == 'Tenessee' and  str(row.abbr) == 'nan' :
        row.abbr  = 'TN'
        
    return row

def q05_replace_missing_values (path1,path2):
    
    df_final = q04_mapping(path1,path2)
    df_final= df_final.apply(update_vals,axis=1)
    return df_final
   







