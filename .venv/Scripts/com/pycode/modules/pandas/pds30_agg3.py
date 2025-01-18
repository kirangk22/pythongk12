import pandas as pd


# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
#coffee=pd.read_csv(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv')

# using github file raw path (open file as raw and take browser path)
#coffee=pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee=pd.read_csv(path)

import numpy as np
# adding new col based on other col case condition
coffee['price']=np.where(coffee['Coffee Type']=='Espresso',3.99,5.99)
coffee['revenue']=coffee['Units Sold']*coffee['price']
print(coffee)


# pivot now...Observe above data
#'Coffee Type' values as columns and corresponding revenue as values for those cols
#print(coffee.pivot(columns=['Coffee Type'],values='revenue'))
print(coffee.pivot(columns=['Coffee Type'],values='revenue',index='Day')) # index is common value for 'Coffee Type'
# here one column values becomes column names        ex: 'Coffee Type'
#       other column values becomes rows(rows vals)  ex: revenue
# here observe 'Day' col val is same/common for above both cols which involved in pivot
# Day is index that's why.....in spark 'Day' is under 'group by'




# So, in summary:
#
# pandas: Uses pivot_table() which combines both grouping and pivoting in one step.
#
# Spark: Uses groupBy() to explicitly group the data and then pivot() to perform the pivot operation.
#
# pivot_df = df.pivot_table(index='ID', columns='Category', values='Value', aggfunc='mean')
#
# pivot_df = df.groupBy("ID").pivot("Category").agg(avg("Value"))
