import pandas as pd
#import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data

path='data/excel-comp-data.xlsx'

def q01_load_data(path):
    data = pd.read_excel(path)
    df1=data['state'].str.lower()
    data['state']=df1
    data['total']=data['Jan']+data['Feb']+data['Mar']
    return data

def q02_append_row(path):    
    df=q01_load_data(path)
    sum_jan=sum(df['Jan'])
    sum_feb=sum(df['Feb'])
    sum_mar=sum(df['Mar'])
    sum_tot=sum(df['total'])
    s = pd.Series([sum_jan, sum_feb, sum_mar, sum_tot], index=['Jan', 'Feb','Mar', 'total'])
    df = df.append(s,ignore_index=True)
    return df


