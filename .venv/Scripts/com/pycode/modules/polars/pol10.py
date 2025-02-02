import polars as pl

# groupby

df = pl.read_csv("./data/output.csv",try_parse_dates=True)
print(df.head())


df1=(df.group_by((pl.col("birthdate").dt.year()//10 * 10).alias("decade"))
     .agg(pl.len().alias("count"),pl.col("weight").mean().alias("avg_wt"),pl.col("height").max().alias("tallest_ht")))
print(df1)