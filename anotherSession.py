# This can be a super spreadsheet to analyze data
# Datas stored in tables also useful extension to python
import pandas as pd
# import os
# print(os.getcwd())
# # To read something like spreadsheet or csv
df = pd.read_csv(r'c:\Users\Sumit Mukharjee\Downloads\Python-For-Data-Analysis\Mall_Customers.csv')
print(df)
# print(display(df))

# first 5 rows
print(df.head())
# last 5 rows
print(df.tail())
print(df.columns)

