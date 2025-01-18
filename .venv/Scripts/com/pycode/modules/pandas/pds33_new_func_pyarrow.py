import pandas as pd

path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\results.csv'
res_numpy=pd.read_csv(path)
res_pyarrow=pd.read_csv(path,engine="pyarrow",dtype_backend="pyarrow")

res_numpy.info()
res_pyarrow.info() # No object datatypes..this is more efficient


# syntax same...but effient using pyarrow
print(res_numpy['as'].str.contains("Keith"))
print(res_pyarrow['as'].str.contains("Keith"))


