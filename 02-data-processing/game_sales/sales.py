import pandas as pd

# Uses: https://www.kaggle.com/migeruj/videogames-predictive-model data file

df = pd.read_csv('dato.csv')

# Allow to display all records of the dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)

print("1. No of games per publisher, sorted")
games_by_publisher_sorted = df.groupby('Publisher')['Platform'].count() \
    .reset_index(name='total').sort_values(['total'], ascending=False)
print(games_by_publisher_sorted)
print("========================================================")

print("2. Max sales in NA")
df['NA_Sales'] = df['NA_Sales'].str.replace(',', '.').astype(float)
sales_per_platform = df.groupby('Platform')['NA_Sales'].sum() \
    .reset_index(name='sum')
max_sales = sales_per_platform.max()
print(max_sales)

print("3. Max sales in Europe")
df['EU_Sales'] = df['EU_Sales'].str.replace(',', '.').astype(float)
sales_per_platform = df.groupby('Platform')['EU_Sales'].sum() \
    .reset_index(name='sum')
max_sales = sales_per_platform.max()
print(max_sales)


#publisher_grouped_df = df.groupby('Publisher')['Platform']

#for key, item in publisher_grouped_df:
#    print(key, ':', len(publisher_grouped_df.get_group(key)))

#publisher_grouped_df['total'] = publisher_grouped_df['Platform'].list.len()
#print(publisher_grouped_df)
