# generators are memory efficient.
# suppose retrive 1million records from DB.using iterators only 1 record at a time loded.
# so memory consumes very less

# yield is like return but not exit the function

def square():   # function which contains yield those are generators.MEMORY efficient
    print("enter def")
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

value=square()

for n in value:
    print(n)


# def square_generator(n):
#     for i in range(n):
#         yield i ** 2
#
# # Example usage:
# n = 10
# squares = square_generator(n)
# for square in squares:
#     print(square)
