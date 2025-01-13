
# List iterate
numbers=[1,2,3,4,5,6]

for n in numbers:
    print(n,end=" ")
print(f"\n============")
for n in reversed(numbers):
    print(n,end=" ")

print(f"\n============")
# Set iterate
numbers={1,2,3,4,5,6,5,6}

for n in numbers:   # set can not be reversed.as its unordered
    print(n,end=" ")

print(f"\n============")

# Tuple iterate
numbers=(1,2,3,4,5,6,5,6)

for n in numbers:
    print(n,end=" ")

print(f"\n============")
dict={'A':'1','B':'2','C':'3'}

for key in dict:
    print(key,end="")
print(f"\n============")
for key in dict.keys():
    print(key,end="")

print(f"\n============")
for val in dict.values():
    print(val,end="")

print(f"\n============")
for key,val in dict.items():
    #print(key,val,end="")
    print(f"{key} = {val}")