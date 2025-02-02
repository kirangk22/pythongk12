import polars as pl
import pol1

df=pol1.df
df.write_csv("./data/output.csv")   # path folders should be available
df_csv = pl.read_csv("./data/output.csv", try_parse_dates=True)
print(df_csv)
