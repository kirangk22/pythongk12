import re

pattern = r'ra'  # Change this pattern as needed
# pattern = r'ar'  # Change this pattern as needed
filtered_lines = []

with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1', 'r') as file:
    for line in file:
        if re.search(pattern, line):
            filtered_lines.append(line.strip())

for line in filtered_lines:
    print(line)
