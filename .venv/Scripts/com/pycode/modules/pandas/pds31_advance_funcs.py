import pandas as pd


# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
coffee=pd.read_csv(path)

import numpy as np
# adding new col based on other col case condition
coffee['price']=np.where(coffee['Coffee Type']=='Espresso',3.99,5.99)
coffee['revenue']=coffee['Units Sold']*coffee['price']
print(coffee)

# add col Prev_revenue using shift()
coffee['prev_rev']=coffee['revenue'].shift(2)  # shift1 previous row, shift2 previous 2nd
print(coffee)


coffee['%_chng']=(coffee['revenue']/coffee['prev_rev'])*100
print(coffee)

# add/calc Cumulative Revenue
coffee['cum_rev']=coffee['revenue'].cumsum()
print(coffee)


# Filter latte types and cal last_3days_revenue
latte_data=coffee[coffee['Coffee Type']=='Latte'].copy()

latte_data['3days_rev']=latte_data['Units Sold'].rolling(3).sum()
print(latte_data)

