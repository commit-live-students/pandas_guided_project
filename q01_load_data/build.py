# %load q01_load_data/build.py
import pandas as pd
path = 'data/excel-comp-data.xlsx'

def q01_load_data(path):
    df = pd.read_excel(path)
    df['total'] = df['Jan']+df['Feb']+df['Mar']
    return df


