import pandas as pd

df_examples = pd.DataFrame(
    data = {
        'col0':[1,3,3,5,1],
        'col1':[7,2,94,37,5],
        'col2':[2,6,-1,10,11]
    }
)
# Columns have to have same aaray length 
# treat it like a 2d grid like excel spreasheet

# print(df_examples)

# getting all rows but specific coolumns

# print(df_examples.loc[:,['col1']]) # all rows but only col1
# print(df_examples.loc[:1,['col1']]) # first 2 rows but only col1
# print(df_examples.loc[:1,['col1','col2']]) # first 2 rows but only col1 and col2

# Masking - another method to get specific rows and columns or datas

my_mask = pd.Series([True,False,True,True,False])
masked = df_examples.loc[my_mask,:]
# print(masked)

# print(~my_mask) # this will return the opposite of the mask basically it negates
print(~masked)
print(~my_mask)

