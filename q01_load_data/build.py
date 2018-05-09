import pandas as pd
path = 'data/excel-comp-data.xlsx'
def q01_load_data(path):
    df = pd.read_excel(path)
    df["state"] = df["state"].str.lower()
    total = df["Jan"]+df["Feb"]+df["Mar"] #total amount in the first quarter of the financial year
    df["total"] = total
    return df
