# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row
def q04_mapping(path1,path2):
    df_clean = pd.read_excel(path1)
    df_scrap =pd.read_csv(path2)
    mapping ={'United States of America':'US'}
    df_clean.insert(loc=6, column='abbr' ,value ='nan')
    df_clean['abbr'].map(mapping)
    return df_clean








