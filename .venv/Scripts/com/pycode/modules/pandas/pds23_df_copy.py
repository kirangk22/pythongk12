import pandas as pd

# READ CSV
path=r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv'
#coffee=pd.read_csv(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\com\pycode\modules\pandas\complete-pandas-tutorial\warmup-data\coffee.csv')

# using github file raw path (open file as raw and take browser path)
#coffee=pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee=pd.read_csv(path)
print(coffee.head())

coffee_new1=coffee  # Both uses/Points to same memory
coffee_new2=coffee.copy()  # both uses different memory now

coffee['price']=5.99
print(coffee)
print(coffee_new1)   # adding col in coffee effects coffee_new1 also
print(coffee_new2)   # not effects as its using diff memory using copy()








