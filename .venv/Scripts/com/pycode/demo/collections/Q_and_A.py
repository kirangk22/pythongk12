
questions=("who is CM of AP?","who is PM of india?","national bird?")

options=(("A.zzz","B.hhh","C.CBN","D.uuu"),
         ("A.NAMO","B.hhh","C.CBN","D.uuu"),
         ("A.zzz","B.hhh","C.CBN","D.Peacock"))

answers=("C","A","D","")
qn=0
your_ans_l=[]
score=0

for q in questions:
    print("------------------------------------")
    print(f"{q}")
    for opns in options[qn]:
        print(opns)

    your_ans=input("enter your answers ")
    your_ans_l.append(your_ans)
    print("=========>",answers[qn])
    if your_ans==answers[qn]:
        print("CORRECT")
        score+=1
    else:
        print("WRONG")
    qn += 1


print("=============RESULTS==================")
print("Answers:",answers)
print("You Ans:",your_ans_l)
print(f"{score} Questions are Correct out of {len(questions)}")