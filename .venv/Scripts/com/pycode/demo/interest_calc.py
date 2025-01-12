p=1000
r=0
t=1  # time in years

while p<=0 or r<=0 or t<=0:
    print("Should not give thease values zero or negetive...")
    p_r_t_vals=input("you want to proceed to chnage vals:(Enter p,r,t)")
    prt_splt=p_r_t_vals.split(",")
    p,t,r=float(prt_splt[0]),float(prt_splt[1]),float(prt_splt[2])

i=p*pow((1+r/100),t)

print(f"The invested amount {p} in {t} yesr will becomes: {i:.2f} ")