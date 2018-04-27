# %load q01_load_data/build.py
import pandas as pd

path = 'data/excel-comp-data.xlsx'
def q01_load_data(path):
    df = pd.read_excel(path)
    df['state']=[x.lower() for x in df['state']]
    df['total'] = df['Jan']+df['Feb']+df['Mar']
    return df
path = 'data/excel-comp-data.xlsx'
df = pd.read_excel(path)
df.state.value_counts()
df.columns.values
df['state']=[x.lower() for x in df['state']]
df['total'] = df['Jan']+df['Feb']+df['Mar']
df['total'].head()
df['Mar'].head()
df.columns.values
df.shape
type(df)


