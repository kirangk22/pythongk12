import random

print(help(random))

print(random.randint(1,100))
print(random.random())  # FOR FLOAT VALS

print(random.randrange(5))

options=["Rock","Paper","Scissiors"]

print(random.choice(options))
random.shuffle(options)
print(options)