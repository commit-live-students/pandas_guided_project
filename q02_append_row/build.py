
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q01_load_data.build import q01_load_data


def q02_append_row(path):
    'write your solution here'
    df = q01_load_data(path)
    sum_row = df[['Jan', 'Feb', 'Mar', 'total']].sum()
    df_sum = pd.DataFrame(data=sum_row).T
    df_final = df.append(df_sum, ignore_index=True)
    return df_final




