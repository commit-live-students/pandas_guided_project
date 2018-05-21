import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q06_sub_total.build import q06_sub_total

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q07_symbols(path1,path2):
    df = q06_sub_total(path1,path2)
    df1 = df.applymap(lambda x: str('$')+str(x))
    df2 = df1.applymap(lambda x: str(x[0:4])+str(',')+str(x[4:]))
    return df2

#q07_symbols(path1,path2)



#print(q07_symbols(path1,path2))
