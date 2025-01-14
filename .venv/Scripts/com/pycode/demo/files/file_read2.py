# Read file into list of lines
with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1', 'r') as file:
    lines_list=file.readlines()

print(lines_list)

# it includes new lines char also

# remove new line char

lines_list=[line.strip() for line in lines_list]
print(lines_list)

# filter lines
lines_list=[line.split(",")[1] for line in lines_list if "kiran" in line]
print(lines_list)