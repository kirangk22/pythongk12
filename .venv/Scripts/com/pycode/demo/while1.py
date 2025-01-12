

name = input("Enter name:")


while name=="":
    print("Enter name please")
    name = input("Enter name:")   # escaping here ..reassign name var..otherwise infinite loop

print(f"Name is: {name}")