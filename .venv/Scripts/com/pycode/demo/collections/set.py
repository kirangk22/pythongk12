# Set  = {} unordered,immutable,but add/remove OK,NO Duplicates

fruits={"apple","banana","oranges","grapes"}

# to see all attributes and methods
print(dir(fruits))
# with description
print(help(fruits))
print(len(fruits))
print("apple" in fruits)


fruits.add("kiwi")
print(fruits)

fruits.add("kiwi")   # removed duplicates...as not allowed
print(fruits)

fruits.remove("kiwi")
print(fruits)


# print(fruits[0])  # [] should not be used for accessing set, because set is unordered.

fruits.pop()  # removes first elements..as its random any can removes
print(fruits)


