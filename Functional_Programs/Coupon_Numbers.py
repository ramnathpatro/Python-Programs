import random
import re
inp = input("How much coupon you want")
generated_cop = []
coupon = 0

x = re.search(r"^[\d]+$", inp)
rang = 1000
if x:
    inp = int(inp)
    if inp <= rang:
        while coupon < inp:
            coupon_gen = random.randrange(rang)
            if coupon_gen not in generated_cop:
                generated_cop.append(coupon_gen)
                coupon += 1
        print(generated_cop)
    else:
        print("Enter valid Number only")
else:
    print("Enter Number only")





