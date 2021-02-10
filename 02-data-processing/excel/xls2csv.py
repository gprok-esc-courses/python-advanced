import pandas as pd
import xlrd

data_xls = pd.read_excel('titanic.xls', 'Sheet1', index_col=None)
data_xls.to_csv('titanic.csv', encoding='utf-8', header=False, index=False)