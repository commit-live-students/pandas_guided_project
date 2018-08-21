# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))


def q03_scrape_clean(url):
    'write your solution here'
    r = requests.get(url, auth=('user', 'pass'))
    df = pd.DataFrame(pd.read_html(r.text)[0]).iloc[12:,:]
    df.to_csv('scrapeddata.csv')
    return df



