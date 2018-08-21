# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
def q03_scrape_clean(url):
    'write your solution here'
    response = requests.get(url)
    df1 = pd.read_html(response.content)[0]
    df1 = df1.iloc[11:, :]
    df1 = df1.rename(columns=df1.iloc[0, :]).iloc[1:, :]
    df1['United States of America'] = df1['United States of America'].apply(lambda x: x.replace(' ', '')).astype(object)
    df1.to_csv('data/scraped.csv')
    return df1


q03_scrape_clean(url)


