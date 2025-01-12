
questions=["who is CM of AP?","who is PM of india?","national bird?"]

options=[["A.zzz","B.hhh","C.CBN","D.uuu"],
         ["A.NAMO","B.hhh","C.CBN","D.uuu"],
         ["A.zzz","B.hhh","C.CBN","D.Peacock"]]

answers=["C","A","D",""]
qn=0

for q in questions:
    print("------------------------------------")
    print(f"{q}")
    for opns in options[qn]:
        print(opns)

    your_ans=input("enter your answers ")
    print("=========>",answers[qn])
    if your_ans==answers[qn]:
        print("CORRECT")
    else:
        print("WRONG")
    qn += 1


