# %load q01_load_data/build.py
import pandas as pd

path = 'data/excel-comp-data.xlsx'
def q01_load_data(path):
    df = pd.read_excel(path)
    df['state'] = df['state'].str.lower()
    df['total'] = df.iloc[:,6:9].sum(axis=1)

    return df

q01_load_data(path)


