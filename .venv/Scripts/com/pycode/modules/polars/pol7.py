import polars as pl
# filter

df = pl.read_csv("./data/output.csv")
print(df.head())


df=df.filter(pl.col("birthdate").str.to_datetime().dt.year()>1990)

print(df)
