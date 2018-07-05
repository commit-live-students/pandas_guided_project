import pandas as pd
import sys, os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data


def q02_append_row(path):
    "write your solution here"
    df = q01_load_data(path)
    return df.append(df.sum(numeric_only=True), ignore_index=True)
