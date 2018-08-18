# %load q01_load_data/build.py
import pandas as pd

def q01_load_data(path):
    'write your solution here'
    df= pd.read_excel(path)
    df.rename(columns={'State':'state'})
    df['total']= df['Jan'] + df['Feb'] + df['Mar']
    
    return df


