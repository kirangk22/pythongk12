import pandas as pd



# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
coffee=pd.read_csv(path)
print(coffee) # All rows and cols

# this itertows not performence..better not use
# this is not pandas specific...Not optimised
for index,row in coffee.iterrows():
    print(index)
    print(row)
    print(f"==============")





# ex 2
for index,row in coffee.iterrows():
    if index==8:
        print(index)
        print(row)
        print(f"==============")

# ex 3
for index,row in coffee.iterrows():
        print(index)
        #print(row["Units Sold"])
        print(row[["Coffee Type","Units Sold"]])
        print(f"==============")

