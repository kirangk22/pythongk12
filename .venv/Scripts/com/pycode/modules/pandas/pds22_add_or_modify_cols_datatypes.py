import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols


print(bios.info())  # to check Datatypes of columns

# Convert types
bios['born_date']=pd.to_datetime(bios['born_date'])
#bios['born_date']=pd.to_datetime(bios['born_date'],format="%Y-%m-%d")
print(bios.info())  # to check Datatypes of columns

# once dataype changes ,we can get flexibility to to use more method ontop of that type
# Add new col born_year , which is extract from born_date

bios['born_year']=bios['born_date'].dt.year  # now can use date functions as datatype chnaged
print(bios[['name','born_date','born_year']])

bios['born_date']=bios['born_date'].dt.strftime('%d-%m-%Y')
print(bios)
