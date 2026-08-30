# import pandas as pd

# # # df = pd.read_csv(r'c:\Users\Sumit Mukharjee\Downloads\Python-For-Data-Analysis\9. Pandas\report.csv')
# # # print(df.head())

# # # import os
# # # print(os.getcwd())

# # # Series is one dimensional labeled array in pandas.
# # # can be created with lists, numpy arrays or dict
# # # it can be as a single column of data with labels or indices for each element

# # data = [10,20,30,40]
# # s  =pd.Series(data)
# # print(s)
# # print(s[2])
# # # by position
# # print(s.iloc[3])
# # print(s[1:4])
# # print(s.shape)

# # # creating dataframes from dictionary
# datas = {'Name':['Alice','Bob'],
#          'Age':[25,30],
#          'City':['New York', 'San Francisco']}
# df = pd.DataFrame(datas)
# # print(df)

# # # Column selection you can select single comum from Dataframe

# # print(df['Name'])

# # # Rows

# # print(df.iloc[2])
# # print(df.iloc[1])

# # # Slicing

# # print(df['Name', 'Age'])
# # # print(df[1:2])

# # # Unique element

# # unique_data = df['Age'].unique()
# # print(unique_data)

# # # conditional

# # above102 = df[df['Age']>25]

# df.to_csv('newframe',index=False)

