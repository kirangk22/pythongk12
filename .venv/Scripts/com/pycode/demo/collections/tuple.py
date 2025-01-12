# tuple = () ordered,immutable,duplicates OK, FASTER than list

fruits=("apple","banana","grapes","oranges","grapes")

# to see all attributes and methods
print(dir(fruits))
# with description
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

print(fruits.index("apple"))
print(fruits.count("grapes"))