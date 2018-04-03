# Load Data and Compute total

We need to find the total amount in the first quarter of the financial year.
Also we need to prepare the data which will be cleaning the text component. 
This exercise is split into two parts. 
 - Prepare the data for further exploration
 - Compute the total amount in the first quarter of the financial year
  

## Write a function `q01_load_data` that :
- Takes the data from the `data folder` and read the excel file using pandas.
- The names of the states `State` column are changed to lower case 
- Create a new column named `total` which computes the total amount in the first quarter
  of the financial year  

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | Path to the excel file in the data folder|

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| df | pd.DataFrame | DataFrame after performing the above operations|
