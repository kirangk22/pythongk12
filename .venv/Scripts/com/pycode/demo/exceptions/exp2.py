a,b=5,0
#a,b=5,2
print("start of prog")

try:
    n=a/b
except Exception as e:
    print(f"Exception occured...Details are{e}")
    print("proceeding with some default values")
    n=100 # some default val
else:
    print("no exception occures...execuing else")
finally:
    print("Finally do some cleanup")


print("Raming code of prog")
print("Final n value is:",n)
