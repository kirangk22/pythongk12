import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [3, 7, 8, 5, 2, 4, 6]
}
df = pd.DataFrame(data)

# Group by 'Category' and get min and max of 'Value' with alias names
result = df.groupby('Category').agg(
    min_value=('Value', 'min'),
    max_value=('Value', 'max')
)

print(result)
