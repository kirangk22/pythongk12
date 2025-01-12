# Collection= single variable used to store multiple values.
# List = [] ordered,mutable(changeble),Duplicates OK
# Set  = {} unordered,immutable,but add/remove OK,NO Duplicates
# tuple = () ordered,immutable,duplicates OK, FASTER

# Dictionary

# to access elements in collection use index [] operator but not for Set

fruits=["apple","banana","oranges","grapes"]
print(fruits)


# Accessing elements
print(fruits[2])

for fruit in fruits:
    print(fruit)

# to see all methods and attributes
print(dir(fruits))

# to see all methods and attributes with description
print(help(fruits))

print("apple" in fruits)


fruits.append("kiwi")
print(fruits)

fruits.insert(1,"water Melon")
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)