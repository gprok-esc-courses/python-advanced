import pandas as pd

df = pd.read_csv('dato.csv')

# Allow to display all records of the dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)

"""
The following code will not actually SUM the NA_Sales column as numbers.
It will sum as strings instead.
Sample output:
    PS2     9,438,416,856,993,012,913,272,712,933,642,451  
"""
sales_per_platform = df.groupby('Platform')['NA_Sales'].sum()
print(sales_per_platform)

"""
Solution: convert to type float.
In our case the sales are in European format so we need to replace the comma to dot first
"""
df['NA_Sales'] = df['NA_Sales'].str.replace(',', '.').astype(float)
sales_per_platform = df.groupby('Platform')['NA_Sales'].sum()
print(sales_per_platform)


