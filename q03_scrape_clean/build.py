# %load q03_scrape_clean/build.py
import pandas as pd

import sys, os
import requests
from bs4 import BeautifulSoup
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
def q03_scrape_clean(url):
    l= []
    headers={'content-type':'text'}
    response = requests.get(url,headers = headers)
    tab = pd.io.html.read_html(url)
    Stoner = tab[0]
    Stoner.drop(Stoner.index[0:11],inplace = True)
    Stoner.reset_index(drop=True, inplace= True)
    header = Stoner.iloc[0]
    df1 = Stoner[1:]
    df1.rename(columns=header,inplace=True)
    df1['United States of America']=df1['United States of America'].apply(lambda x : (x.split('[')[0]))
    df1.to_csv('scrapeddata.csv')
    return df1
    


    

q03_scrape_clean('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')
                
                
            


