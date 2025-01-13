# A concise way of cretaing Lists in python.
# Formula:    [expression for value in iterable if condition]


# without List comrehention
doubles=[]

for i in range(1,11):
    doubles.append(i*2)
print(doubles)

# with List comprehention above can be written as..
# doubles=[expression for value in iterable if condition]
doubles=[i*2 for i in range(1,16)]
print(doubles)


fruits=["Apples","Oranges","Banana"]
# create a list to convert above list values in capitals
fruits=[fruit.upper() for fruit in fruits]
print(fruits)

#create a list having first letters of above list values
first_let=[fruit[0] for fruit in fruits]
print(first_let)


nums=[1,4,-5,6,-8,9,-7]
# cretae list of +ve nums
pos_l=[n for n in nums if n>=0]
print(pos_l)
# cretate list of -ve nums
neg_l=[n for n in nums if n<0]
print(neg_l)
