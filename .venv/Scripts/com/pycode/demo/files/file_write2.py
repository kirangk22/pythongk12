lines = ["First line.\n", "Second line.\n", "Third line.\n"]

with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1_w', 'w') as file:
    file.writelines(lines)


# Read from a file and write into another
with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1', 'r') as file:
    file_lines_list=file.readlines()

import re
pattern = r'ra'
filtered_lines_list=[line for line in file_lines_list if re.search(pattern, line)]
print(f"filtered list of lines are:{filtered_lines_list}")

with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test2_w', 'w') as file:
    file.writelines(filtered_lines_list)