import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)

# Custom function to apply case conditions
def age_category(age):
    if age < 30:
        return 'Young'
    elif age < 40:
        return 'Middle-aged'
    else:
        return 'Senior'

# Applying the custom function to the 'Age' column
df['Category'] = df['Age'].apply(age_category)

print(df)
