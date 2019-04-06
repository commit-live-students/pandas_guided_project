import pandas as pd
import sys, os
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

def q02_append_row(path):
    df = q01_load_data(path)
    df1 = df[['Jan', 'Feb', 'Mar', 'total']].sum(axis=0)
    df1 = pd.DataFrame(df1)
    df2 = pd.DataFrame(columns=['Jan', 'Feb', 'Mar', 'total'])
    df2['Jan'] = df1.loc['Jan']
    df2['Feb'] = df1.loc['Feb']
    df2['Mar'] = df1.loc['Mar']
    df2['total'] = df1.loc['total']
    df3 = df.append(df2, ignore_index=True)


