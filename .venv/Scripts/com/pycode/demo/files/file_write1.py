with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1_w', 'w') as file:
    file.write("This is a line of text.\n")
    file.write("This is another line of text.")


with open(r'C:\Users\admin\PycharmProjects\pythonProject2\.venv\Scripts\Test1_w', 'a') as file:
    file.write("\nThis line will be appended to the file.")
