import pandas as pd


# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\bios.csv'
bios=pd.read_csv(path)
print(bios)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# add col height_rank using rank()
bios['height_rank']=bios['height_cm'].rank()
print(bios.sort_values(['height_rank'],ascending=False))

# same above
bios['height_rank']=bios['height_cm'].rank(ascending=False)
print(bios.sort_values(['height_rank']))  # asc True vals..as need rank 1 first


# print(bios.sort_values(['height_rank']).sample(10)[['name','height_rank']])
# print(bios.sort_values(['height_rank'])[['name','height_rank']].sample(10))
print(bios.sort_values(['height_rank'])[['name','height_rank']].head(10))