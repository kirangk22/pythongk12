import pandas as pd

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'

coffee=pd.read_csv(path)
print(coffee.head()) # First 5 rows
print(coffee)   # shows All rows

print(coffee.head(10)) # First 10 rows
print(coffee.tail()) # Last 5 rows
print(coffee.tail(10)) # Last 10 rows

print(coffee.sample()) # acess/show Randon data
print(coffee.sample(4)) # acess/show Randon data..random 4 records here..each run records chnages

print(coffee.sample(4,random_state=1)) # acess/show Random data..random 4 records here..each run no chnage of data here


print(coffee.loc[10])
print(coffee.loc[10:10])
print(coffee.loc[10:10,['Day','Coffee Type']])
print(coffee.columns)
print(coffee)
print(coffee.loc[10:,["Day","Units Sold"]])
