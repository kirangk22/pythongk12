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


#    drop with inplace attrib usage
print(coffee.drop(columns=['price'],inplace=True))
print(coffee)  # Now NOT shows price col

# calc revenue per each day...add new col revenue
coffee['revenue']=coffee['Units Sold']*coffee['new_price']
print(coffee)


# Rename cols
# df.rename(columns={key:val dict})

print(coffee.rename(columns={'new_price':'PRICE'}))

