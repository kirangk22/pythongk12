import pandas as pd

# loc iloc
# df.loc[rows,cols]
# df.iloc[rows,cols]  # only using index values in cols also
# *** df.ixxx always expect int values (.iloc,iat)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
coffee=pd.read_csv(path)
print(coffee) # All rows and cols

# change value @ specific row ,col value
# assign/update 1 indexed row related 'Units Sold' as 150
coffee.loc[1,"Units Sold"]=150
print(coffee.loc[1:1])  # show just 1 loc index row...updated value as 150

# update multiple rows
coffee.loc[1:5,"Units Sold"]=150  # 1 to 5 indexed rows,updinf 'Units Sold' as 150
print(coffee)










