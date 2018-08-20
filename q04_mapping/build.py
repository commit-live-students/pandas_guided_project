# %load q04_mapping/build.py
import pandas as pd
import sys, os
import numpy as np
#I added below 4 lines
from greyatomlib.pandas_guided_project.q01_load_data.build import q01_load_data
import requests
import csv
from bs4 import BeautifulSoup
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
# I commented below line
#from greyatomlib.pandas_guided_project.q02_append_row.build import q02_append_row

def q02_append_row(path):
    data_set = q01_load_data(path)
    data_set.at['Grand Total', 'Jan'] = data_set['Jan'].sum()
    data_set.at['Grand Total', 'Feb'] = data_set['Feb'].sum()
    data_set.at['Grand Total', 'Mar'] = data_set['Mar'].sum()
    data_set.at['Grand Total', 'total'] = data_set['total'].sum()    
    return data_set

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
    return df1


def q04_mapping(path1,path2):
    df_from_appended_row = q02_append_row(path1)    
    df_from_scraped_data = q03_scrape_clean(path2)

    '''Approach 1 for creating a dictionary
    mapping = df_from_scraped_data.set_index('United States of America').to_dict()['U.S.']
    '''
    '''Approach 2 for creating a dictionary
    '''
    mapping = dict(zip(df_from_scraped_data['United States of America'].str.lower(), df_from_scraped_data['U.S.']))

    df_final = df_from_appended_row
    #Inseting 'abbr' at column 6 - Approach 2 for this is given below
    df_final.insert(6, 'abbr', '')
    '''Approach 1
    Advantage of this approach is if there are no matching keys in the dictioinary, then the column values are mapped to NaN
    '''
    df_final['abbr'] = df_final['state'].str.lower().map(mapping)

    '''Approach 2
    df_final['abbr'] = df_final['state'].str.lower().replace(mapping)
    df_final.loc[df_from_appended_row['abbr'] == df_final['state'],'abbr'] = float('nan')
    '''
    
    '''Approach 2 for ordering columns on a specified index
    Reindexing the columns can also be done using reindex_axis method.
    df_final = df_final.reindex_axis(['account', 'name', 'street', 'city', 'state', 'postal-code', 'abbr', 'Jan', 'Feb', 'Mar', 'total'], axis=1)    
    '''
    return df_final
    

