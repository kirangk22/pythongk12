import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols
print(bios.info())  # to see cols and datatypes info

# Shorthand Method to Filter Data....USEFUL
# same above without loc method
print(bios[bios["height_cm"] > 215]) # Filter data based on some condition
print(bios[bios["height_cm"] > 215][["name","height_cm"]]) # condition+[selected cols list]

# multiple conditions   df[(cond1) & (cond2)]
print(bios[(bios["height_cm"]>215) & (bios["born_country"]=="USA")])

print(bios[:5]) # filter only 5 first rows
print(bios[:5][["name","height_cm"]]) # filter only 5 first rows and select few cols