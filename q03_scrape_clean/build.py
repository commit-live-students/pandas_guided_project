
import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
def q03_scrape_clean(url):
    'write your solution here'
    r =requests.get(url)
    df = pd.read_html(r.text, header=0)
    #df_1 = df[0]
    #names = ['United States of America', 'Federal state', 'US USA 840', 'US', , '', '', 'U.S', 'U.S.']
    df_1 = pd.DataFrame(df[0])
    df_1.drop(df_1.index[range(10)], inplace=True)
    header=df_1.iloc[0]
    df_1 = df_1[1:]
    df_1.columns = header
    #df_1.rename(columns = header)
    #df_1.ix[~(iris['sepal length (cm)'] < 5)]
    #df_1.ix[df_1.index < 10]
    value = ''
    df_1=df_1.fillna(value)
    #df_1.columns = df_1.fillna(value)
    df_2 = df_1.to_csv('scrapeddata.csv')
    return (df_1)
            
q03_scrape_clean(url)


