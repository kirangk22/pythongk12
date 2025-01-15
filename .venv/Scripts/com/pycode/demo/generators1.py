# generators are memory efficient.
# suppose retrive 1million records from DB.using iterators only 1 record at a time loded.
# so memory consumes very less

def topten():
    yield 1
    yield 2
    yield 3
    yield 4    # yield is like return but not exit the function

value=topten()
print(type(value))


for n in value:
    print(n)