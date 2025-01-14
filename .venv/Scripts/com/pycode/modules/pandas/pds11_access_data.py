import pandas as pd

# at ,iat are for to get single value from DF.not for multiple vals
# *** df.ixxx always expect int values (.iloc,iat)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
coffee=pd.read_csv(path)
print(coffee) # All rows and cols



# just to get specific value at any postion fo DF
# 0th index row,'Units Sold' col value
print(coffee.at[0,"Units Sold"])

print(coffee.iat[0,2])  # i always expects int values , here 0th loc row,2nd col value

# mostly we use loc,iloc only....but ave option of at,iat to get single vals at specific position of DF

print(coffee.iloc[0,2])   # i always expects int params
print(coffee.loc[0,"Units Sold"])

# at,iat may be some efficient
