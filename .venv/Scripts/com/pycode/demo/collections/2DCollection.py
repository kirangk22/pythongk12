# List of Lists...nested Lists.

fruits=["appple","banana","kiwi"]
vegs=["tomato","potato","brinjal"]
meat=["fish","chicken","beaf"]

grocerry=[fruits,vegs,meat]

print(grocerry[1])
print(grocerry[1][0])

for item in grocerry:
    print(item)


for item in grocerry:
    for val in item:
        print(val," ",end="")
    print()