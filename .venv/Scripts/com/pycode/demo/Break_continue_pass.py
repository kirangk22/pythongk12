# break used in loops . to jump out of loops
# continue used in loops. to skip current iteration and continue next iteration in loop
# pass. just used when no need to print anything in any function,if conditions...etc

av = 10
x = int(input("Enter candys that u want:"))
i = 1

while i <= x:
    if i > av:
        break
    print("candy", i)
    i += 1

print("Bye")

for i in range(1, 21):
    if i % 2 != 0:
        continue  # skip current iteration and go to next iteration
    print(i)

for i in range(1, 21):
    if i % 2 != 0:
        pass  # nothing to do just pass
    else:
        print(i)
