
"""
******************************************************************************
* Purpose:  There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
*           returned by Vending Machine. Write a Program to calculate the minimum
*           number of Notes as well as the Notes to be returned by the Vending
*           Machine as aChange
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""


import re
from Algorithm_Programs.utility import algorithm
ref = algorithm



def vending_machine():
    inps = input("Enter the amount")

    cheack = re.search(r"^[\d]+$", inps)
    if cheack:
        inps = int(inps)
        ref.countCurrency(inps) # cal the notes calling function and pass theargument
    else:
        print("Enter proper amount")

if __name__ == '__main__':
    vending_machine()