import polars as pl

df=pl.read_csv("./data/output.csv") #  datatype is string for date cols
print(df.head())
# print(df.describe())



df=pl.read_csv("./data/output.csv",try_parse_dates=True)  # now datatype is date
print(df.head())
# print(df.describe())