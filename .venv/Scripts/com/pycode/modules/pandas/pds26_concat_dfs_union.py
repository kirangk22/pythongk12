import pandas as pd



#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# READ bios CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios) # All rows and cols

usa=bios[bios['born_country']=='USA'].copy()
gbr=bios[bios['born_country']=='GBR'].copy()

print("USA count:",len(usa))
print("GBR count:",len(gbr))

# Now combine both usa and gbr datasets (union)
usa_gbr=pd.concat([usa,gbr],axis=0) # axis=0 default means combine rows
print("USA+GBR :",len(usa_gbr))         # axis=1 means combine cols


print(usa_gbr)
