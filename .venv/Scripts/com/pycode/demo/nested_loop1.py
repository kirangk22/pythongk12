## nested loops: a loop inside another loop

rows=int(input("Enter Rows:"))
cols=int(input("Enter cols:"))

for x in range(rows):
    for y in range(cols):
        print("*",end="")
    print()