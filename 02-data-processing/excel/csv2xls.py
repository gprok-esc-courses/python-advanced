import pandas as pd
import xlwt

csv_file = pd.read_csv('titanic.csv')
xls_file = pd.ExcelWriter('titanic.xls')
csv_file.to_excel(xls_file, index=False)
xls_file.save()
