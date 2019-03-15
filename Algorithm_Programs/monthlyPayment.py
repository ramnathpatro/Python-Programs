import re
from Algorithm_Programs.utility import algorithm

ref = algorithm

def monthly_payment():
    P1 = input("Enter the principal loan")
    Y1 = input("Enter the Year")
    R1 = input("Enter the interest")
    cheack_P = re.search(r"^[\d]+$", P1)
    cheack_Y = re.search(r"^[\d]{1}$", Y1)
    cheack_R = re.search(r"^[\d]{2}|[\d]{1}$", R1)

    if cheack_P and cheack_R and cheack_Y:
        P = int(P1)
        Y = int(Y1)
        R = int(R1)
        print(ref.payment(P, Y, R))

    else:
        print("Wrong input")

if __name__ == '__main__':
    monthly_payment()



