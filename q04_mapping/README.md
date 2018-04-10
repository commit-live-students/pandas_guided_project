# Mapping Countries to their abbreviations

In this assignment you will use the data scraped from the previous assignment and map abbriviation to the 
name of states.
 
  

## Write a function `q04_mapping` that :
- Uses the return of `q02_append_row` and also `q03_scrape_clean` 
- Using the scraped data create a dictionary called `mapping` which has the Country
 as key and Abbreviation as value
-  Create a new column called `abbr` as the 6th column of the DataFrame 
returned from `q02_append_row`
- Using the Dictionary `mapping` map the names of the states to fill in the abbr
### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path1 | string | compulsory |  | Path to the excel file in the data folder|
| path2 | string | compulsory |  | Path to the csv file in the data folder|
### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df_final| pd.DataFrame | DataFrame after performing the above operations|
