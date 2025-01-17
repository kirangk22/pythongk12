import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2','A3'],
    'B': ['B0', 'B1', 'B2','B3']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
})

print("df1 data:\n",df1)
print("df2 data:\n",df2)
# Concatenate along rows
result = pd.concat([df1, df2], axis=0)  # axis=0 for rows default
print("combined data (by rows)\n",result)
print(len(result))

result = pd.concat([df1, df2], axis=1)  # axis=1 for cols
print("combined data (by cols)\n",result)
print(len(result))