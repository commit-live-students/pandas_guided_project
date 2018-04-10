# Append a row to the DataFrame

In this assignment we will append a row to the data frame which will give us information 
about the total amount of all the users for the month of jan feb and march and also the grand total
 
## Write a function `q02_append_row` that :
- Uses the function `q01_load_data` from the previous assignment
- Computes the sum of amount of all users in the Month of Jan, Feb, March and the Grand total 
 (Here the sum implies the sum of all the entries in the `Jan Column`, sum of entries in `Feb` Column and Grand total stands for the sum of entries in the column `total`)
- Append this computed sum to the DataFrame 

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the excel file in the data folder|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df_final | pd.DataFrame | DataFrame after performing the above operations|
