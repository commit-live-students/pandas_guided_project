import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
def q05_replace_missing_values(path1,path2):
    df = q04_mapping(path1,path2)
    df.iloc[6,6] = 'MS'
    df.iloc[10,6] = 'TN'
    return df


#q05_replace_missing_values(path1,path2)
