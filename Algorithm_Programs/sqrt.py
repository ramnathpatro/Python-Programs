
"""
******************************************************************************
* Purpose:  calculate the Newton_sqrt
* @author:  Ramnath Patro
* @version: 1.0
* @since:   13-3-2019
*
******************************************************************************
"""

import math
import re
from Algorithm_Programs.utility import algorithm
ref = algorithm


def Newton_sqrt():
    c_inp = input("Enter nonnegative Number")
    cheack = re.search(r"^[\d]+$", c_inp)

    if cheack:
        c_inp = int(c_inp) # convert str to int
        print("numberis", c_inp, "surt", ref.Newton_sqrt(c_inp))
    else:
        print("Enter Number only")


if __name__ == '__main__':
    Newton_sqrt()


