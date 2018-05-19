import pandas as pd

def q01_load_data(path):
    path='data/excel-comp-data.xlsx'
    data = pd.read_excel(path)
    #data['state']= map(lambda x: x.lower(), data['state'])
    df1=data['state'].str.lower()
    data['state']=df1
    data['total']=data['Jan']+data['Feb']+data['Mar']
    return data


