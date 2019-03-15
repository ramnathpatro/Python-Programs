import re
# define a function
def print_factors(x):
   # This function takes a number and prints the factors
    print("The factors of",x,"are:")
    list_fact = []

    for i in range(1, x + 1):
        if x % i == 0:

            list_fact.append(i)
    return list_fact
# change this value for a different result.
#num = 320

# uncomment the following line to take input from the user
num = input("Enter a number: ")
if re.search(r"^[\d]+$",num):
    inp = int(num)
    print(print_factors(inp))
else:
    print("Enter Number only")

