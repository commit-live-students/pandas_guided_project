# %load q03_scrape_clean/build.py
import pandas as pd
import re
import sys, os
import csv
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'

def q03_scrape_clean(url):
    #data_from_page = requests.get(url)
    list_of_tables = pd.read_html(url, header = 0, skiprows = 11, attrs = {'class' : 'wikitable sortable'})
    df1 = pd.DataFrame(list_of_tables[0])
    df1 = df1.rename(columns = {'.mw-parser-output .monospaced{font-family:monospace,monospace}USUSA840' : 'US USA 840'})
    df1['United States of America'] = df1['United States of America'].str.replace(' ', '')    
    df1.to_csv('..\data\scrapeddata.csv', index = False)
    
    return df1
    
q03_scrape_clean(url)



