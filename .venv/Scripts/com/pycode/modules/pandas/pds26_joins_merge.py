import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ bios CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols

# READ NOC csv noc_regions.csv
noc_path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\noc_regions.csv'
noc_reg_data=pd.read_csv(noc_path)
print(noc_reg_data)

# now check data above join bios.born_country with noc_reg_data.NOC
# how= default inner, use whatever needed join
joined_df=pd.merge(bios,noc_reg_data,left_on='born_country',right_on='NOC',how='left')
print(joined_df)
# after join if any duplicate columns are there,those comes with suffix x,y
# we can use our own suffix if needed.

# rename based on need
joined_df.rename(columns={'region':'born_country_full'},inplace=True)

print(joined_df)

# Filter rows where NOC_x != born_country_full

print(joined_df[joined_df['NOC_x']!=joined_df['born_country_full']][['name','born_country','NOC_x','born_country_full']])