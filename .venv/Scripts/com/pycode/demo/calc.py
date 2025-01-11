operator=input("Enter operator (+ - / *)")
n1=float(input("Enter first num:"))
n2=float(input("Enter second num:"))

#print(f"{n1 + n2}")

if operator=="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
else:
    print("others...")
