import polars as pl
import datetime as dt
# filter   is_between

df = pl.read_csv("./data/output.csv")
print(df.head())


df=df.filter(pl.col("birthdate").str.to_datetime().is_between(dt.date(1982,12,31),dt.date(1996,12,31)))

print(df)
