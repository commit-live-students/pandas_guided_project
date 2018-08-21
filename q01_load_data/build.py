# %load q01_load_data/build.py
import pandas as pd
path = 'data/excel-comp-data.xlsx'

def q01_load_data(path):
    'write your solution here'
    df = pd.read_excel(path)
    df['state'] = df['state'].apply(lambda x: x.lower())
    df['total'] = df['Jan'] + df['Feb'] + df['Mar']
    return df

q01_load_data(path)

