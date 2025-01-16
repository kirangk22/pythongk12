import pandas as pd

# usage of :  string operations and Regex to filter Data

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)



# Filter born_country in USA,FRA
print(bios[bios['born_country'].isin(['USA','FRA'])])

# Filter born_country in USA,FRA and name starts with Keith
print(bios[(bios['born_country'].isin(['USA','FRA'])) & (bios['name'].str.startswith("Keith"))])

print(bios.query("born_country == 'USA' and born_city=='Seattle'"))

