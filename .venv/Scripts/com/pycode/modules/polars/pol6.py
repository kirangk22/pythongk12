import polars as pl
# with_columns ---> to add or modify cols

df = pl.read_csv("./data/output.csv")
print(df.head())



res=df.with_columns(
    name=pl.col("name"),
# birth_year=pl.col("birthdate").str.strptime(pl.Datetime, "%Y-%m-%d").dt.year(),
    birth_year=pl.col("birthdate").str.to_datetime().dt.year(),
    bmi=(pl.col("weight") / (pl.col("height") ** 2))
)

print(res)


