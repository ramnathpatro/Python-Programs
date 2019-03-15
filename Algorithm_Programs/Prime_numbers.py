
"""
******************************************************************************
* Purpose:  Find 0- nth number of prime Number
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""


import re
from Algorithm_Programs.utility import algorithm
p1 = algorithm
def prime():
    inp = input("Enter number only")
    check_int = re.search(r"^[\d]+$", inp)
    if check_int:
        inp = int(inp)
        print(algorithm.prime_number(inp))
    else:
        print("Enter Number only not String")

if __name__ == '__main__':
    prime()


