import re

inp = input("Enter the Number")
cons = 1
x = re.search(r"^[\d]+$",inp)
cons = 0

if x:
    inp = int(inp)
    if inp > 0:
        for num in range(1,inp+1):
            cons+=1/num

        print(cons)
    else:
        print("Invalid Number")
else:
    print("Enter the Number only")