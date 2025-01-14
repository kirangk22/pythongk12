import pandas as pd



# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
coffee=pd.read_csv(path)
print(coffee) # All rows and cols


print(coffee["Day"])
print(coffee.Day)    # can access using dot . for cols of NO SPace
print(coffee["Units Sold"])  # here space in col name. so can't access using dot.


print("=======>access List of selected Cols")
print(coffee[["Day","Units Sold"]])

print(coffee.sort_values("Units Sold"))  # default asc order
print(coffee.sort_values("Units Sold",ascending=0)) # asc False..so desc order


# here "Coffee Type" asc True and "Units Sold" Asc False(desc)
print(coffee.sort_values(["Coffee Type","Units Sold"],ascending=[1,0]))


