import polars as pl

# groupby

df = pl.read_csv("./data/output.csv",try_parse_dates=True)
print(df.head())


df1=df.with_columns(
     (pl.col("birthdate").dt.year()//10 * 10).alias("decade")
)

print(df1)

df2=df.with_columns(
     (pl.col("birthdate").dt.year()//10 * 10).alias("decade"),
     pl.col("name").str.split(" ").list.get(0).alias("first_name")
)

print(df2)

df3=df.with_columns(
     (pl.col("birthdate").dt.year()//10 * 10).alias("decade"),
     pl.col("name").str.split(" ").list.get(0).alias("first_name")
).select(
     pl.all().exclude("birthdate")
)

print(df3)


df4=(df.with_columns(
     (pl.col("birthdate").dt.year()//10 * 10).alias("decade"),
     pl.col("name").str.split(" ").list.get(0).alias("first_name")
).select(
     pl.all().exclude("birthdate")
).group_by(pl.col("decade"))
     .agg(pl.col("weight","height").mean().name.suffix("_avg")))

print(df4)


df5=(df.with_columns(
     (pl.col("birthdate").dt.year()//10 * 10).alias("decade"),
     pl.col("name").str.split(" ").list.get(0).alias("first_name")
).select(
     pl.all().exclude("birthdate")
).group_by(pl.col("decade"))
     .agg(
     pl.col("name"),
     # pl.col("first_name"),
     pl.col("weight","height").mean().name.suffix("_avg")))

print(df5)