# iterators used to fetch 1 value at a time.

l=[1,2,3,4]

it=iter(l) # iter() func to convert list to iter obj


# 2 ways __next or next()...both same
print(it.__next__()) # gets 1st values in iter obj
print(it.__next__()) # now point moves to 2nd values and gets
print(next(it))
