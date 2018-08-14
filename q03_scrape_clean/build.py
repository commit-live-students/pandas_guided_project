# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))



def q03_scrape_clean(url):
    data = requests.get(url)
    mlist = pd.read_html(data.text)
    df = mlist[0]
    df = df[11:-1]
    df.to_csv('./data/scrapeddata.csv')
    return df







