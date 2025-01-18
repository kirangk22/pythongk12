import pandas as pd


# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios)

bios.info()  # to see cols and datatypes
bios['born_date']=pd.to_datetime(bios['born_date'])
bios.info()


# print(bios[bios['died_date'].isna()])

# ex1
print(bios.groupby(bios['born_date'].dt.year)['name'].agg('count'))
print(bios.groupby(bios['born_date'].dt.year)['name'].agg('count').reset_index())
print(bios.groupby(bios['born_date'].dt.year)['name']
      .agg('count').reset_index().sort_values('name',ascending=False))


# ex2
bios['born_year']=bios['born_date'].dt.year
bios['born_month']=bios['born_date'].dt.month

print(bios.groupby([bios['born_year'],bios['born_month']])['name']
      .agg('count').reset_index().sort_values('name',ascending=False))

# same result as above using Dictionary on agg()
print(bios.groupby([bios['born_year'],bios['born_month']])
      .agg({'name':'count'}).reset_index().sort_values('name',ascending=False))

# same result as above using Dictionary on agg()...Alias names ** Best Approch **
print(bios.groupby([bios['born_year'],bios['born_month']])
      .agg(cnt=('name','count')).reset_index()
      .sort_values('cnt',ascending=False))

# Formula
# df.groupby([col1,col2])
#       .agg(cnt_als1=('col','agg_func'),cnt_als2=('coln','agg_func'))
#       .sort_values('cnt_als1',ascending=False)

