import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ bios CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols

# READ results.csv
path_r=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\results.csv'
results=pd.read_csv(path_r)
print(results)

# now check data above join bios.athlete_id with results.athlete_id  (joined col name same on both dfs)
# how= default inner, use whatever needed join
joined_df=pd.merge(results,bios,on='athlete_id',how='left')
#left_on='',right_on='' not needed as col name is same on both dfs
print(joined_df)
# after join if any duplicate columns are there,those comes with suffix x,y
# we can use our own suffix if needed.


