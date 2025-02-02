import polars as pl

# str to date casting   and try_parse_dates=True usage
# https://docs.pola.rs/user-guide/expressions/casting/#parsing-formatting-temporal-data-types

# df = pl.read_csv("./data/output.csv")
# print(df.head())

df = pl.read_csv("./data/output.csv",try_parse_dates=True)
# df=df.select(pl.col("name"),pl.col("birthdate").dt.year().alias("birth_year"),
#           (pl.col("weight")/pl.col("height")**2).alias("BMI"))

result = df.select(
    pl.col("name"),
    # pl.col("birthdate").str.strptime(pl.Datetime, "%Y-%m-%d").dt.year().alias("birth_year"),
    # pl.col("birthdate").str.to_datetime().dt.year(),
    pl.col("birthdate").dt.year(),
    (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
)
print(result)


