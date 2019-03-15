import re

inp = input("Enter the power between 0 to 31")
cons = 1
x = re.search(r"^[\d+]{1,2}$",inp)
#print(x.group())
if x:
    inp = int(inp)
    if inp >= 1 and inp < 31:
        print(2 ** inp, "power of 2 the ", inp)
    else:
        print("invalid Number")
