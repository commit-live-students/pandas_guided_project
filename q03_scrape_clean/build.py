# %load q03_scrape_clean/build.py
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from bs4 import BeautifulSoup

def q03_scrape_clean(url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'):
    a=requests.get(url)
    soup=BeautifulSoup(a.content,'html.parser')
    stat=soup.find_all('table',class_='wikitable')[0]#.tbody.tr.decompose()
    #stat.tbody.tr.decompose()
    df=pd.read_html(str(stat))[0]
    df=pd.DataFrame(df)
    df=df[9:]
    df=df.drop([10,9,11])#<--Directly pass a number and not a list for a single row
    df=df.reset_index(drop=True)
    df[0].str.replace(' ','')
    return df


#     rows=stat[0].tbody.find_all('tr')
#     headers=stat[0].tbody.find_all('td')
#     for row in rows:
#         for cell in headers:
            
#     res=requests.get(url)
#     soup=BeautifulSoup(res.content,'lxml')
#     table=soup.find_all('table')[0]
#     return table
    
   
            
    
    


c=q03_scrape_clean(url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')
c



