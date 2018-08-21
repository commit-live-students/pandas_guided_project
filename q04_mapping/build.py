import pandas as pd
import sys, os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q02_append_row.build import q02_append_row
def q04_mapping(path1,path2):
    'write your solution here'
    df_final= q02_append_row(path1)
    scraped = pd.read_csv(path2)
    scraped['United States of America'] = scraped['United States of America'].astype(str).apply(lambda x: x.lower())
    scraped['US'] = scraped['US'].astype(str)
    mapping = scraped.set_index('United States of America')['US'].to_dict()
    df_final.insert(6, 'abbr', np.nan)
    df_final['abbr'] = df_final['state'].map(mapping)
    return df_final




