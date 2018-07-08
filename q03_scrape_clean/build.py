# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'

def q03_scrape_clean(url):
    data = requests.get(url)
    df = pd.read_html(data.text)[0]
    df=df.iloc[11:, :]
    df=df.rename(columns= df.iloc[0,:])
    df1= df.iloc[1:,:]
    df1.to_csv('data/scrapeddata.csv')
    return df1
    
q03_scrape_clean(url)  

