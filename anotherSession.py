# # This can be a super spreadsheet to analyze data
# # Datas stored in tables also useful extension to python
# import pandas as pd
# # import os
# # print(os.getcwd())
# # # To read something like spreadsheet or csv
# df = pd.read_csv(r'c:\Users\Sumit Mukharjee\Downloads\Python-For-Data-Analysis\Mall_Customers.csv')
# print(df)
# # print(display(df))

# # first 5 rows
# print(df.head())
# # last 5 rows
# print(df.tail())
# print(df.columns)
# # df = 'CustomerID';
# # method a to acess
# print(df.CustomerID)

# # method b to acess
# print(df['CustomerID'])

# print(df['Genre'])

# customer_id = df.CustomerID
# # Series is a specialised dict
# print(type(customer_id))
# print(customer_id[10])

# # can create own dict

# population_dict = {
#     "California":234564,
#     "Seattle":232332,
#     "Texas":223563,
#     "Florida":2114554
# }

# population = pd.Series(population_dict)
# print(population)
# print(type(population))



import pandas as pd
df = pd.read_csv(r'c:\Users\Sumit Mukharjee\Downloads\Python-For-Data-Analysis\Mall_Customers.csv')
names = df['Genre']
print(type(names))

# Using the .loc() method, assign the Age and Math Grade columns for the first 30 rows of df to a variable called first_thirty_loc.

# th Grade
# # Your code here
# first_thirty_loc = df.loc[df.index[:30],['Age','Math Grade']]
# # your code here

# even numbered rows assingment on two variables

# even_numbered_rows = df.loc[0:2,['Name','Emglish_grade']]