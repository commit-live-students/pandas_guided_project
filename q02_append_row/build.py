# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path = './data/excel-comp-data.xlsx'

def q02_append_row(path):
    df = q01_load_data(path)
    total_jan = df['Jan'].sum()
    total_feb = df['Feb'].sum()
    total_mar = df['Mar'].sum()
    total_grand = df['total'].sum()

    df2 = pd.DataFrame(columns= df.columns)
    df2['Jan'] = [total_jan]
    df2['Feb'] = [total_feb]
    df2['Mar'] = [total_mar]
    df2['total'] = [total_grand]
    df = df.append(df2, ignore_index=True)
    return df








