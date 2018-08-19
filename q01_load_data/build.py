# %load q01_load_data/build.py
import pandas as pd

path = 'data/excel-comp-data.xlsx'
def q01_load_data(path):
    data = pd.read_excel(path)

    data['state'] = data.state.str.lower()
    data['total'] = data[['Jan','Feb','Mar']].sum(axis=1)

    return data




