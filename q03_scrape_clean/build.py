# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
def q03_scrape_clean(url):

    from urllib.request import urlopen

    df = pd.read_html(url, skiprows = 11,header = 0)
    df[0] = df[0].rename(columns = {'United States of America':'UnitedStatesofAmerica'})
    data_folder = df[0].to_csv('scrapeddata.csv')
    return df[0]

q03_scrape_clean(url)


