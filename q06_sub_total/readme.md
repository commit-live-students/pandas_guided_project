# Filling in the Missing Values

Great Job so far!

Now lets move on and use the newly created abbr column to understand the total amount that the bank holds in each state.
 
  

## Write a function `q06_sub_total` that :
- Uses the return of `q05_replace_missing_value`  
- groups by `abbr` and finds the sum

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path1 | string | compulsory |  | Path to the excel file in the data folder|
| --- | --- | --- | --- | --- |
| path2 | string | compulsory |  | Path to the csv file in the data folder|
### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df_sub| pd.DataFrame | DataFrame after performing the above operations|

