with open('C:\\Users\\admin\\PycharmProjects\\pythonProject2\\.venv\\Scripts\\Test1', 'r') as file:
    data = file.read()
    print(data)

# using raw string path
with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1', 'r') as file:
    data = file.read()
    print(data)

print("===============================")
# Reading the File Line by Line:
with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1', 'r') as file:
    for line in file:
        print(line.split(",")[0],"=",line.split(",")[1])



print("===============================")