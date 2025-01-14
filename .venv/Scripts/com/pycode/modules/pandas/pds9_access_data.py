import pandas as pd

# loc iloc
# df.loc[rows,cols]
# df.iloc[rows,cols]  # only using index values in cols also

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
coffee=pd.read_csv(path)
print(coffee.head()) # First 5 rows
print(coffee) # All rows and cols

#print(coffee.loc[#rows,[#cols list]])

# undersnad #rows below
print(coffee.loc[0]) # get row at 0th location/index ...vertical show
print(coffee.loc[[0]]) # get row at 0th location/index ...horizontal show
print("====>")
print(coffee.loc[[0,1,5]]) # get rows at specific locs

# slice/index syntax
print(coffee.loc[0:3])  # 0th row to 3rd row records
print(coffee.loc[5:])  # 5th row to all n records
print(coffee.loc[0:8:2])  # starts with 0th row then step by 2 records and show
print(coffee.loc[13::-1])  # Rows with reverse order
print(coffee.loc[5:9])  # 5th loc row to 9th loc row records

# undersnad #rows with # cols below
#print(coffee.loc[#rows,[#cols list]])
print(coffee.loc[[0],["Day"]])  # shows 0th loc row with 'Day' col
print(coffee.loc[0,"Day"])  # shows 0th loc row with 'Day' col
print(coffee.loc[5:8,["Day","Units Sold"]])  # 5-8 loc rows, specific list of cols
print(coffee.loc[10:,["Day","Units Sold"]])  # 10 to all n loc rows, specific list of cols

# below 2 aare same loc, iloc access
print(coffee.loc[:,["Day","Units Sold"]])  # All Rows but specific cols

print(coffee.iloc[:,[0,2]])  # All Rows but specific cols based on index
                             # oth column is 'Day' and 2nd index cols is 'Units Sold'


#use specific col values as index cols instead of 0,1,2,3..etc
coffee.index=coffee["Day"]   # using Day col values as index
coffee.index=coffee.Day   # can access cols using dot .
print(coffee)  # no numerical values at index now

# now try to access below...no numeric at index now...Day col values are there
#print(coffee.loc[0:3])  # accessing 0th loca to 3rd loc rows but now no numeric locations ..it Fails
print(coffee.loc["Monday"])   # accessing index loc which has Monday...filter Monday data

print(coffee.loc["Monday":"Tuesday"])   # accessing rows of index loc from Monday to Tuesday


###print(coffee.loc[#row, [#cols]])
print(coffee.loc["Monday":"Wednesday",["Units Sold"]])   # accessing rows of index loc from Monday to Wednesday
                                                        # and specific cols only






