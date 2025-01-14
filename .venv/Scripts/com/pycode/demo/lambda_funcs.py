# lambda function is a small anonymous func for one time use (temparory)
# usage :   lambda_func_name = lambda parameter:expression


double=lambda x:x*2
print(double(8))  # while calling pass params required for lambda func


add=lambda x,y:x+y
print(add(4,8))

min=lambda x,y:x if x<y else y
print(min(3,7))

age=lambda n:"Adult" if n>=18 else "Child"
print(age(17))

day=lambda d:{print(d)}
print(day("sunday"))

