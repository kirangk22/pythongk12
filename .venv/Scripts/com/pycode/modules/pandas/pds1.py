import pandas as pd

#help(pd)
# understand the functions and others in pandas file modules

#pd.DataFrame([[row1 list of vals],[row2],[row3]]) # list of lists
df=pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']])
print(df)

df=pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']],columns=['C1','C2','C3'])
print(df)
print(df.index.to_list())  # to show incdex numbers

df=pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']],columns=['C1','C2','C3'],index=['x','y','z'])
print(df.index.to_list())  # now index chnages from numbers to x,y,z

print(df.head())
print(df.head(2)) # to see first 2 rows

print(df.tail(2)) # to see last 2 rows
print(df.columns)

