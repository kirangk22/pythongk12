import  pandas as pd

path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\data\olympics-data.xlsx'

olympic_data=pd.read_excel(path)  # reads first sheet by default
print(olympic_data.head())


# Read specific sheet
olympic_data_res=pd.read_excel(path,sheet_name="results")
print(olympic_data_res.head())