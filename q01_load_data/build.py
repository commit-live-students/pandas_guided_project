import pandas as pd

path = 'data/excel-comp-data.xlsx'
def q01_load_data(path):
    'write your solution here'
    df = pd.read_excel(path)
    df['total'] = pd.to_numeric(df['Jan']) + pd.to_numeric(df['Feb']) + pd.to_numeric(df['Mar'])
    return (df)
q01_load_data(path)


