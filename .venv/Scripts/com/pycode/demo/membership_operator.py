# Membership operator =  used to test a value or variable is found in sequence
#                       (String,List,Set,Tuple,Dictionary)
#                       1.in   2.not in
#


# check a letter in string
name="Aplle"

if "p" in name:
    print("Letter found")
else:
    print("Letter not found")



email="xyz@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid Email")


# chekcinh nay one of List,tiple,Set

Students={"kiran","kumar","ravi","raj","hari"}

student="raji"
if student in Students:
    print("Found Student")
else:
    print("Not Found")

# chekc dict

grades={"kiran":"A",
        "raj":"B",
        "kumar":"A",
        "ravi":"D"}

stud="kiran"
if stud in grades:  # it checks keys by default in dict
    print(f"grade of student is:{grades.get(stud)}")