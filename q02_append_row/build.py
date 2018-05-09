import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
path = 'data/excel-comp-data.xlsx'

def q01_load_data(path):
    df = pd.read_excel(path)
    df["state"] = df["state"].str.lower()
    df['total'] = df.sum(axis=1)
    return df

def q02_append_row(path):
    df = q01_load_data(path)
    sum_row=df[["Jan","Feb","Mar","total"]].sum() #sum for the month and total columns.
    df_sum=pd.DataFrame(data=sum_row).T #Converting the series into a dataframe and transposing it
    df_sum=df_sum.reindex(columns=df.columns) #using reindex to add the missing values
    df_final=df.append(df_sum,ignore_index=True)
    return df_final
