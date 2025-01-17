import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols

# add new col 'ht_catg' using height_cm
bios['ht_ctg'] = bios['height_cm'].apply(lambda x:"Short" if x<165 else ("Avg" if x<185 else "Tall"))
# here apply method takes one col 'height_cm' values
print(bios[['name','height_cm','ht_ctg']])


# ex 2============================
# add new cols 'athlet_ctg'
def athlet_ctg(row):
    if row['height_cm']<170 and row['weight_kg']<70:
        return "LowerWeight"
    elif row['height_cm']<180 or row['weight_kg']<80:
        return "AVG_Weight"
    else:
        return "HeavyWeight"


# here apply() take entire row of dataframe
bios['athlet_ctg']=bios.apply(athlet_ctg,axis=1)
# axis=1 means rows.....passing one by one rows of dataframe
# axis=0 means cols in apply()

print(bios)
