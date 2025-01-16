import pandas as pd

# usage of :  string operations and Regex to filter Data

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)


# filter Keith name rows
print(bios[bios["name"].str.contains("Keith")])
print("Rows count:",len(bios[bios["name"].str.contains("Keith")]))
print(bios[bios["name"].str.contains("kEiTh",case=False)]) # case False


# filter rows that 'name' col contains Keith or patrick (Regex usage)
print(bios[bios["name"].str.contains(r"Keith|patrick",case=False)])
print(bios[bios["name"].str.contains(r"Keith|patrick",case=False,regex=False)]) # turnoff Regex option

# pd.set_option('display.max_rows', None)
# Filter names ending with Son|sen
print(bios[bios["name"].str.contains(r"Son$|sen$",case=False)])

# Filter born_date starts with 19
#print(bios[bios["born_date"].str.contains(r"^19")]) # # error: containing NA / NaN values
print(bios[bios["born_date"].str.contains(r"^19",na=False)])  # to handling No values (NA / NaN values)

# Filter born_country in USA,FRA
print(bios[bios['born_country'].isin(['USA','FRA'])])

