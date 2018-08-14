# %load q02_append_row/build.py
import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
path =  'data/excel-comp-data.xlsx'

def q02_append_row(path):
    df = q01_load_data(path)
    t1 = pd.DataFrame(df['Jan']).sum()
    t2 = pd.DataFrame(df['Feb']).sum()
    t3 = pd.DataFrame(df['Mar']).sum()
    t4 = pd.DataFrame(df['total']).sum()
    Total = [t1,t2,t3,t4]
    df2 = pd.DataFrame(columns=df.columns)
#     df2.loc[0] = df2['Jan'].append(t1)
#     df2.loc[0] = df2['Feb'].append(t2)
#     df2.loc[0] = df2['Mar'].append(t3)
    df2.loc[0] = df2['Jan'].append(Total)
    df_final = pd.concat([df, df2],ignore_index=True)
    
    return df_final

#q02_append_row(path)




