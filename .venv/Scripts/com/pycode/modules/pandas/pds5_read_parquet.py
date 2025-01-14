import pandas as pd

print("# READ PARQUET (efficient)")
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\results.parquet'
res_df=pd.read_parquet(path)
print(res_df.head())

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(res_df.head())