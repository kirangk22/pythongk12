# Accessing sequence of elements using [] index operator
#[start:end:step]  start postion is inclusive and end position is exclusive

card="1234-5675-67543-7895"

print(card[0])
print(card[4])

print(card[0:4])
print(card[::-1]) # reerse string...start to end from last char onwards

print(card[::3])  # 3rd char

print("xxxx-xxxx-xxxx-"+card[-4:])
