import pandas as pd


# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
#coffee=pd.read_csv(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv')

# using github file raw path (open file as raw and take browser path)
#coffee=pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee=pd.read_csv(path)
print(coffee)

coffee['price']=5.99
print(coffee.groupby('Coffee Type').sum(['Units Sold']))

print(coffee.groupby('Coffee Type').mean(['Units Sold']))

print(coffee.groupby('Coffee Type').agg({'Units Sold':'sum','price':'mean'}))

print(coffee.groupby(['Day','Coffee Type']).agg({'Units Sold':'sum','price':'mean'}))


# multiple functions on diff cols
# here below each key should be unique otherwise it takes last key logic
print(coffee.groupby(['Coffee Type','Day']).agg({'Units Sold':'sum',
                                           'price':'mean'
                                           }))  #  'Units Sold':'max','Units Sold':'min'


# mutiple agg function on single col
print(coffee.groupby(['Coffee Type','Day'])['Units Sold'].agg(['min','max']))
print(coffee.groupby(['Day'])['Units Sold'].agg(['min','max']))
print(coffee.groupby(['Day'])[['Units Sold','price']].agg(['min','max']))


# Formula:
# df.groupby([list_of_cols][[list_of_selected_cols_for aggn]].agg([agg funs]))




