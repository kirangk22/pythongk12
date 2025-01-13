# dictionaries: a Collection of {key,value} pairs
# ordered ,changable. NO Duplicates.


capitals={"USA":"Washington","India":"New Delhi","china":"Beijing"}

print(dir(capitals))
print(help(capitals))

print(capitals.get("India"))

capitals.update({"NEW1":"New1xyz"})
capitals.update({"china":"Beiging"})

print(capitals)

capitals.pop("china")
print(capitals)


capitals.popitem()  # removes last added item
print(capitals)



print(capitals.keys())
print(capitals.values())
print(capitals.items())


# iterate on top of dict
for key,val in capitals.items():
    print(key,val)


