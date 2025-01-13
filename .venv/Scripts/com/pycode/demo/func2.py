# return : statemnet used to end function and send
#          result back to the caller.


def add(x,y):
    z=x+y
    return z

print(add(2,8))




def arth_op(x,y,op):
    switch={
        '+':x+y,
        '-':x-y,
        '*':x*y
    }
    return switch.get(op)

print(arth_op(2,3,"+"))
print(arth_op(2,3,"-"))
print(arth_op(2,3,"*"))

