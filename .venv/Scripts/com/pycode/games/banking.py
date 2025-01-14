
bal=0
is_running=True
def show_balance():
    print(f"Balce is:{bal}")

def deposit(d_amt):
    global bal
    bal=bal + d_amt
    print(f"Depositing amt{d_amt}\nBalance after Deposit is:{bal}")


def withdraw():
    pass



# def main():
while is_running:
    print(f"==================================================\n 1. show balance \n 2.deposit \n"
          f"3.withdraw \n 4.Exit")
    choice=input("Enter the option that you like (1,2,3,4)")

    match choice:
        case "1":
            show_balance()
        case "2":
            d_amt=float(input("Enter deposit amt:"))
            deposit(d_amt)
        case "3":
            pass
        case "4":
            is_running = False
            print("Thank you for using")

        case _:
            print("invalid option")





# while is_running:
#     if __name__=="__main__":
#         main()
#     print("====>",is_running)
