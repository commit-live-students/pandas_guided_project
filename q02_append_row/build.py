# %load q02_append_row/build.py
import pandas as pd
import numpy as np
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data


def q02_append_row(path):
    'write your solution here'
    df = q01_load_data(path)
    sum_row = df[['Jan', 'Feb', 'Mar', 'total']].sum()
    return df.append(sum_row, ignore_index=True)


q02_append_row('data/excel-comp-data.xlsx')

