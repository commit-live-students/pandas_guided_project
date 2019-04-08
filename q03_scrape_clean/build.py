import pandas as pd
import sys, os
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))


def q03_scrape_clean(url):
    page = requests.get(url)
    
    df = pd.read_html(page.text)
    df1 = df[0].iloc[11:,0]
    df2 = df[0].iloc[11:,1]
    df3 = df[0].iloc[11:,2]
    df4 = df[0].iloc[11:,3]
    df5 = df[0].iloc[11:,4]
    df6 = df[0].iloc[11:,5]
    df7 = df[0].iloc[11:,6]
    df8 = df[0].iloc[11:,7]
    df9 = df[0].iloc[11:,8]
    df10 = df[0].iloc[11:,9]
    
    ans = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10], axis=1)
    ans.rename(mapper={0:'Name', 1:'Status', 2:'ISO', 3:'ANSI0', 4:'ANSI1', 5:'USPS', 6:'USCG', 7:'GPO', 8:'AP', 9:'Other Abbrevations'}, inplace=True, axis=1)
    ans.drop(ans.index[0], axis=0, inplace=True)
    ans['ex1'] = 0
    ans['ex2'] = 0
    ans['ex3'] = 0
    ans['ex4'] = 0
    ans['ex5'] = 0

