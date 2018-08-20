# Scrape Data From the web 

In this assignment you will be scraping data from the web and cleaning it. 
 
  

## Write a function `q03_scrape_clean` that :
- Scrapes the url `https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations` and pick up
the right table
- use module `requests` to `get` the url and use pandas to read_html
- First few rows consists of unclean data. You need to select rows from index 11 till end. Make the values at index 11 as column headers.
- Remove space from the column named 'United States of America'
- Save it to the scraped data to data folder and name it `scrapeddata.csv`


### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the excel file in the data folder|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df1 | pd.DataFrame | DataFrame after performing the above operations|
