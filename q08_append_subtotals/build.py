import pandas as pd
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q06_sub_total.build import q06_sub_total
from q07_symbols.build import q07_symbols


path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def comma(x):
    if len(str(x)) == 6:
        x = str(x)
        return str('$')+str(x[0:3])+str(',')+str(x[3:])

    elif len(str(x)) == 5:
        x = str(x)
        return str('$')+str(x[0:2])+str(',')+str(x[2:])

    elif len(str(x)) == 7:
        x = str(x)
        return str('$')+str(x[0])+str(',')+str(x[1:4])+str(',')+str(x[4:])

def q08_append_subtotals(path1,path2):
    df = q06_sub_total(path1,path2)
    jan = df['Jan'].sum()
    feb = df['Feb'].sum()
    mar = df['Mar'].sum()
    t = df['total'].sum()
    a = df['account'].sum()
    temp = pd.DataFrame({'Jan':[jan],'Feb':[feb], 'Mar':[mar], 'account':[a], 'total':[t]})
    df2 = df.append(temp,ignore_index=True)
    dfy = df2.applymap(comma)
    dfy.drop('account', axis=1, inplace=True)
    return dfy

#q08_append_subtotals(path1,path2)
