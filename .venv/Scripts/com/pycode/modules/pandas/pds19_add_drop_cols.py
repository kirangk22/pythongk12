import pandas as pd

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
#coffee=pd.read_csv(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv')

# using github file raw path (open file as raw and take browser path)
#coffee=pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee=pd.read_csv(path)
print(coffee.head())


# add new col price
coffee['price']=4.99
print(coffee)

# new_price for each coffee Types
# Espresso 3.99 ,Latte 5.99

import numpy as np
coffee['new_price']=np.where(coffee['Coffee Type']=="Espresso",3.99,5.99)
print(coffee)
#df['new_price']=np.where(df['col_n']=="Espresso",Truecase,Falsecase)


# drop cols or rows
# Formauls :
# df.drop(index number of row)
# df.drop([index number of rows])
# df.drop(columns=[list of cols to drop])
# droping 0th index Row
print(coffee.drop(0))
print(coffee.drop(8))  # drop 8th index row

print(coffee.drop([1,5,10])) # drop multiple rows based on index val
#print(coffee.loc[5:]) # drop first 5 rows


# drop Cols
print(coffee.drop(columns=['price']))
print(coffee)  # still shows price col

print(coffee.drop(columns=['price'],inplace=True))
print(coffee)  # Now NOT shows price col

#coffee=coffee[[list_of_cols_toselected]]

coffee=coffee[['Day','Units Sold',]]  # otherway of dropping cols
print(coffee)