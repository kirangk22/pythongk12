
# to see all function sof string data type
print(help(str))

name="kiran kumar"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.find("k",0))

print(name.rfind("k",0))

print(name.count("k"))
print(name.count("k",0,4))

print(name.replace("kiran","g kiran"))

print(name.replace("k","A",1))


print("1-234-567-8910".count("-"))