# %load q02_append_row/build.py
#import pandas as pd
#import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
#from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
#from q01_load_data.build import q01_load_data
#path = 'data/excel-comp-data.xlsx'


#import pandas as pd
#import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))


'''
def q02_append_row(path):
    'write your solution here'
    df = q01_load_data(path)
    sum_row = df[['Jan', 'Feb', 'Mar', 'total']].sum()
    df_sum = pd.DataFrame(data=sum_row).T
    df_final = df.append(df_sum, ignore_index=True)
    return df_final
'''
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
#from q01_load_data.build import q01_load_data
path = 'data/excel-comp-data.xlsx'
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
    return df3




q02_append_row(path)

