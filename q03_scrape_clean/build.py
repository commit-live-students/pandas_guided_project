# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
from bs4 import BeautifulSoup
sys.path.append(os.path.join(os.path.dirname(os.curdir)))


def q03_scrape_clean(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    df = df.iloc[12:,:]

    return df

q03_scrape_clean('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')


