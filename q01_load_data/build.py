# %load q01_load_data/build.py
import pandas as pd


def q01_load_data(path):
    df=pd.read_excel(path)
    #df['state'] = map(lambda x: x.upper(), df['state'])
    df['state'] = df['state'].str.upper()
    df['total']=df['Jan']+df['Feb']+df['Mar']
    return df

path = 'data/excel-comp-data.xlsx'
#print(q01_load_data(path))

