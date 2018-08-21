# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

def q03_scrape_clean(path):
    df1= pd.read_html(requests.get(path).text)
    df = df1[0]
    df_new = df[11:]
    df_header = df_new[1:]
    header = df_new.iloc[0]
    df_header.rename(columns = header,  inplace=True)
    df_header.rename(columns = {'United States of America':'UnitedStatesofAmerica'},  inplace=True)
    return df_header





