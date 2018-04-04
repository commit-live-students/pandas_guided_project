# Append a row to the DataFrame

In this assignment we will append a row to the data frame which will give us information 
about the total amount of the various regions in jan feb and march and also the grand total
 
## Write a function `q08_append_subtotals` that :
- Uses the function `q06_sub_total` from the previous assignment
- Computes the sum of amount of all users in the Month of Jan, Feb, March and the Grand total 
 (Here the sum implies the sum of all the entries in the `Jan Column`, sum of entries in `Feb` Column and Grand total stands for the sum of entries in the column `total`)
- Make sure you append the `$` to all the digits.
- Append this computed sum to the DataFrame 

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path1 | string | compulsory |  | Path to the excel file in the data folder|
| path2 | string | compulsory |  | Path to the csv file in the data folder|


### Returns:
| Return | dtype | description |
| --- | --- | --- |
| final_table | pd.DataFrame | DataFrame after performing the above operations|
