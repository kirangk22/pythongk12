name=input("Enter valid name: ")

if not name.isalpha():
    print("digits not allowed")
elif name.find(" ")>1:
    print("spaces not allowed")
elif len(name)>12:
    print("name should be lessthan 12 chars")
else:
    print(f"valid useranme {name}")
