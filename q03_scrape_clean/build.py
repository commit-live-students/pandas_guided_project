# %load q03_scrape_clean/build.py
import pandas as pd
import re
import sys, os
import csv
import requests
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'

def q03_scrape_clean(url):
    data_from_page = requests.get(url)
    page_text = data_from_page.text
    data_soup = BeautifulSoup(page_text, 'lxml')
    table_data = data_soup.find('table', class_='wikitable sortable')

    column_names = []
    list_of_rows = []
    i = 0
    #Skipping the first table row element since we dont want it in our data frame
    for row in table_data.find_all('tr')[9:]:
        head_tags = row.findAll('th')
        if(len(head_tags) > 0):
            for column in head_tags:
                column_names.append(column.find(text=True))

        list_of_cells = []
        data_tags = row.findAll('td')
        if(len(data_tags) > 0):
            for row_data in data_tags:
                row_text = row_data.text.strip()
                '''if(len(row_data.find_all('a')) > 0):
                    #print ('Length of a is: ', len(row_data.find_all('a')))
                    #print ('Text of a is: ', row_data.find('a').text)
                    row_text = row_data.find('a').text
                elif(len(row_data.find_all('style')) > 0):
                    row_text = row_data.find('span').text
                else:
                    row_text = row_data.find(text=True)
                '''
                list_of_cells.append(row_text)
            i = i + 1
            #print ('Row is: ', list_of_cells)
            list_of_rows.append(list_of_cells)
    
    outfile = open('D:\GreyAtom\Guided_Project\Scraped_Data\scrapeddata.csv', 'w', newline='')
    writer = csv.writer(outfile)
    for row_for_csv in list_of_rows:
        if(row_for_csv.__contains__('.mw-parser-output .monospaced{font-family:monospace,monospace}USUSA840')):
            index_data = row_for_csv.index('.mw-parser-output .monospaced{font-family:monospace,monospace}USUSA840')
            row_for_csv.remove('.mw-parser-output .monospaced{font-family:monospace,monospace}USUSA840')
            row_for_csv.insert(index_data, 'US USA 840')
        writer.writerow(row_for_csv)
    outfile.flush()
    outfile.close()
    
    df1 = pd.read_csv('D:\GreyAtom\Guided_Project\Scraped_Data\scrapeddata.csv')
    df1['United States of America'] = df1['United States of America'].str.replace(' ', '')

    # % new empty columns are added to match the dataframe results
    df1[''] = ''
    df1[' '] = ''
    df1['  '] = ''
    df1['   '] = ''
    df1['    '] = ''
    print (type(df1))
    print (df1.shape)
    return df1
q03_scrape_clean(url)



