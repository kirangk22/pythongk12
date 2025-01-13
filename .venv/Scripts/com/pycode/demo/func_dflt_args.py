# def calc_price(act_prc,tax1,tax2):
#     return act_prc+tax1+tax2

def calc_price(act_prc,tax1=1,tax2=0):  # assign default values to args.if no args passed thease will used.
      return act_prc+tax1+tax2

print(calc_price(250,1,2))
print(calc_price(250))

