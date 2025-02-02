import polars as pl
# concat

df1 = pl.read_csv("./data/output.csv")
print(df1)

df2 = pl.read_csv("./data/output2.csv")
print(df2)


joined_df=df1.join(df2,on="name",how="inner")  # joined col name is same "name" on both dfs

print(joined_df)


df3 = pl.read_csv("./data/output3.csv")
print(df3)                                  # joined col name is diff "name" on both dfs
joined_df3=df1.join(df3,left_on="name",right_on="full_name",how="inner")
print(joined_df3)

# in output joined col always shows onetime only.

