# Filling in the Missing Values

What you will notice in the previous assignment is that for two states Mississippi and Tennessee 
will have NaN values in column `abbr`. In this assignment you will be filling those missing values
manually. 
 
  

## Write a function `q05_replace_missing_values` that :
- Uses the return of `q04_mapping`  
- Locate the NaN in the abbr and replace it 

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path1 | string | compulsory |  | Path to the excel file in the data folder|
| --- | --- | --- | --- | --- |
| path2 | string | compulsory |  | Path to the csv file in the data folder|
### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df_final| pd.DataFrame | DataFrame after performing the above operations|
