tmp=float(input("Enter given temp : "))
units=input("Units of the temp that entered is:(C or F) ")

if units=="C":
    tmp=(9*tmp)/5+32
    units="F"
elif units=="F":
    tmp=5/9*(tmp-32)
    units="C"
else:
    print("invalid input")

print(f"Converted temp is:{tmp} {units}")