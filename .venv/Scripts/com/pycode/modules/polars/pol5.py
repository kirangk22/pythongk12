import polars as pl
# select

df = pl.read_csv("./data/output.csv")
print(df.head())

# showing 95% of wt,ht...removing 5 %
result = df.select(
    pl.col("name"),
    (pl.col("weight","height")*0.95).name.suffix("-5%")

)
print(result)


