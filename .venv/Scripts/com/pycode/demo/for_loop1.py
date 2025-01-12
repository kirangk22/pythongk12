# Execute block of code fixed number of times.
# u can iterate over a range,string,sequence,...etc


for i in range(1,11):  # start inclusive and end exclusive in range
    print(i)

for i in reversed(range(1,11)):
    print(i,"...")
print("Happy new year")


for i in range(1,11,2):    # start,end,step
    print(i)

card="1234-12345-8754-9876"
for i in card:
    print(i)

for i in range(1,21):
    if i==13:
        continue    # skip or ignoring 13 value in loop
    else:
        print(i)

for i in range(1,100):
    if i==26:
        break    # break loop.come out of loop
    else:
        print(i)