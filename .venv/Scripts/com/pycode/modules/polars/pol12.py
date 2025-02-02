import polars as pl
# concat

df = pl.read_csv("./data/output.csv")
print(df.head())


df1=(df.filter(pl.col("birthdate").str.to_datetime().dt.year()>1990)
     .with_columns(pl.col("name").str.split(" ").list.get(0)))

print(df1)

# concat
print(pl.concat([df,df1],how="vertical"))
