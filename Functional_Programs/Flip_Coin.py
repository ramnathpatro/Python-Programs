import re
import random

inp = input("how many time you flip the coin")

heads = 0
tails = 0
flip_coin = 0

check = re.search(r"^[\d]+$", inp)
#print(check.group())

if check:
    inp = int(inp)
    while flip_coin < inp:
        flip_coin += 1
        coin_tos = random.randrange(2)
        if coin_tos == 0:
            heads += 1

    print("Head is", heads / inp * 100, "%")
    print("Tails", 100 - heads / inp * 100, "%")

else:
    print("Enter the Number only")



