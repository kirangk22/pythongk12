import polars as pl

# groupby

df = pl.read_csv("./data/output.csv",try_parse_dates=True)
print(df.head())

df1=df.group_by(pl.col("birthdate").dt.year().alias("B_YEAR")).count()
print(df1)

# `GroupBy.count` is deprecated. It has been renamed to `len`.
df2=df.group_by(pl.col("birthdate").dt.year().alias("B_YEAR")).len()
print(df2)


df3=df.group_by(pl.col("birthdate").dt.year().alias("B_YEAR"),maintain_order=True,).len()
print(df3)

# The keyword argument maintain_order forces Polars to present the resulting groups
# in the same order as they appear in the original dataframe.