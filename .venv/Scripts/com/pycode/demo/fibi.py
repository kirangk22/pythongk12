terms=10
n1=0
n2=1
c=0

while c<terms:
    print(n1,end=" ")
    n1,n2=n2,n1+n2    #1
    c+=1


# def fibonacci(n):
#     n1, n2 = 0, 1
#     for i in range(n):
#         print(n1,end=" ")
#         n1, n2 = n2, n1 + n2
#
# # Example usage
# n = 10 # Number of terms
# fibonacci_series = fibonacci(n)

