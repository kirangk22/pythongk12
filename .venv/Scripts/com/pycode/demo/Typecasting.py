# process of converting datatype of variable to another type
#str() float() int() bool()
name="kiran"
print(type(name))
print(name)
print(f"name value given ? {bool(name)}")


age=35
print(f"age in int:{age} and age in float:{float(age)}")

height=155.5
print(f"height in float:{height} and in int :{int(height)}")

x,y=10,20
print(x+y)

x=str(x)
y=str(y)
print(x+y)