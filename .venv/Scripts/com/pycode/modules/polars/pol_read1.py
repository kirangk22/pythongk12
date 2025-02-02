import polars as pl

df=pl.read_csv("./data/pokemon_data.csv")
print(df.head())
print(df.describe())



# Foloo
# https://docs.pola.rs/user-guide/getting-started/#select