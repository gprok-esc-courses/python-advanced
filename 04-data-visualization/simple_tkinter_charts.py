from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Example from: https://datatofish.com/matplotlib-charts-tkinter-gui/

# GDP Per Capita
data_gdp = {'Country': ['US', 'CA', 'DE', 'UK', 'FR'],
            'GDP': [45000, 42000, 52000, 49000, 47000]}
df_gdp = DataFrame(data_gdp, columns=['Country', 'GDP'])
print(df_gdp)

# Unemployment rate
data_unemployment = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                     'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]}
df_unemployment = DataFrame(data_unemployment, columns=['Year', 'Unemployment_Rate'])
# print(df_unemployment)

# Invest rate
data_invest = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
               'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
               }
df_invest = DataFrame(data_invest, columns=['Interest_Rate', 'Stock_Index_Price'])
# print(df_invest)

# Create the window app
root= tk.Tk()

figure1 = plt.Figure(figsize=(5, 6), dpi=100)
ax1 = figure1.add_subplot(221)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df_gdp_country = df_gdp[['Country','GDP']].groupby('Country').sum()
print(df_gdp_country)
df_gdp_country.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure1.add_subplot(224)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df_unemployment = df_unemployment[['Year', 'Unemployment_Rate']].groupby('Year').sum()
df_unemployment.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(data_invest['Interest_Rate'], data_invest['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')

root.mainloop()
