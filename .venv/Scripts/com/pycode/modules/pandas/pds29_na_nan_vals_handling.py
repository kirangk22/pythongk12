import numpy as np
import pandas as pd

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
#coffee=pd.read_csv(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv')

# using github file raw path (open file as raw and take browser path)
#coffee=pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee=pd.read_csv(path)
print(coffee.head())
coffee1=coffee.copy()

coffee.loc[0:2,['Units Sold']]=np.nan
print(coffee)

# can check df has null values or not
coffee.info()  # it shows total entries and non-null entries counts

print(coffee.isna().sum()) # shows each columns how many nulls there with counts


# fill null na cols with some default values
print(coffee.fillna(100))  # null values populated with 100

print(coffee.fillna(coffee['Units Sold'].mean())) # fill with mean value based on other vals in same col

coffee1.loc[2:3,['Units Sold']]=np.nan
print(coffee1)
print(coffee1.fillna(coffee['Units Sold'].interpolate()))

print(coffee1.dropna()) # drops null rows..any cols contain null drops that entite row

print(coffee1.dropna(subset=['Units Sold'])) # only drop rows if units sold is null..not consider other col nulls


# Filter rows which contains 'Units Sold' col having null
print(coffee[coffee['Units Sold'].isna()])

print(coffee[coffee['Units Sold'].notna()])  # not null rows filter

