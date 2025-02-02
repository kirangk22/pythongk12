# head tail sample glimpse describe

import polars as pl

# joined col name is same "name" on both dfs

path=r"C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\polars\data\output.csv"
# df=pl.read_csv(path)
df=pl.read_csv(path,try_parse_dates=True)

print(df.head(2))
print(df.tail(3))
print(df.glimpse())
print(df.sample(4))
print(df.describe())

print("======================================")
print(df)   # shows all data of df
print(df.select(pl.all()))   # shows all data of df..same like above
print(df.select(pl.all().exclude("weight","height")))