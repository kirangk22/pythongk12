import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols

# Add New col First name using name col
bios['first_name']=bios['name'].str.split(' ').str[0]
print(bios)

# modify Existed col  name using name col yo hold firstname
bios['name']=bios['name'].str.split(' ').str[0]
print(bios)

print(bios.query("first_name=='Keith'"))

print(bios.info())  # to check Datatypes of columns

bios['born_date']=pd.to_datetime(bios['born_date'])
print(bios.info())  # to check Datatypes of columns