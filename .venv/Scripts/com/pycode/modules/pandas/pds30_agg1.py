import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ bios CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols

print(bios.value_counts()) # each record count shows
print(bios['born_city'].value_counts())


# filter USA data then select one col and get value counts on that col
print(bios[bios['born_city']=='USA']['born_region'].value_counts())

