def full_name(first,middle,last):
    return first.capitalize()+" "+middle.capitalize()+" "+last.capitalize()


print(full_name("kiran","kumar","gande"))

print(full_name(last="Gande",first="kiran",middle="kumar"))  # keyword args