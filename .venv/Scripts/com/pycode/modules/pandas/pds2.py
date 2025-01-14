import pandas as pd

df=pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']],columns=["C1","C2","C3"])
df.info() # info along with memory usage
print(df.size) # total no.of items in df

my_data=[['1','2','3'],['4','5','6'],['7','8','3']]
df1=pd.DataFrame(my_data,columns=['C1','C2','C3'])
print(df1)

print(df1.describe())

print(df1.nunique())  # to show unique vals in each col
print(df1['C1'].unique())  # to show unique vals in column C1
print(df1.shape)  # shows x rows and y cols

print(df1[['C1','C3']]) # df[list_of_cols to show]

