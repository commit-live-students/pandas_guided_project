# %load q01_load_data/build.py
import pandas as pd
path = 'data/excel-comp-data.xlsx'

def q01_load_data(path):
    'write your solution here'
    data = pd.read_excel(path)
    data['state'] = data['state'].map(lambda x: x if type(x)!=str else x.lower())
    data['total'] = data.Jan + data.Feb + data.Mar
    return data



