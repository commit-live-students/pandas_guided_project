# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))


def q03_scrape_clean(url):
    'write your solution here'
    response = requests.get(url)
    result = pd.read_html(response.text)
    df = result[0][11:-1]
    #df = df[0].str.strip()
    df.to_csv('./data/scrapeddata.csv')
    return df

q03_scrape_clean('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')





