wt=float(input("Enter Weight"))
units=input("units of wt (K or L)")

if units=="K":
    wt=wt*2.20462
    units="lbs"
elif units=="L":
    wt=wt/2.20462
    units="kgs"
else:
    print(f"invalid unit types {units}")

print(f"Converted wt is:{wt} {units}")