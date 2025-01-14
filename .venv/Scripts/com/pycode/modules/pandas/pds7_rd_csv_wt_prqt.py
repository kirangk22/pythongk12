import pandas as pd

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'

coffee=pd.read_csv(path)
#print(coffee.head())


w_path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\csv_to_par.parquet'
coffee.to_parquet(w_path)


print(pd.read_parquet(w_path).head())