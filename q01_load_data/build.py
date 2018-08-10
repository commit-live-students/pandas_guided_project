# %load q01_load_data/build.py
import pandas as pd
import numpy as np

def q01_load_data(path='data/excel-comp-data.xlsx'):
    #'write your solution here'
    df=pd.read_excel(path)
    df=pd.DataFrame(df)
    df['state']=df['state'].str.lower()#Series column lower case syntax is str.lower()
    df['Total']=df['Jan']+df['Feb']+df['Mar']#+ operator works coz its overloaded
    return df

c=q01_load_data(path='data/excel-comp-data.xlsx')
c.shape




