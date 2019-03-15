
"""
******************************************************************************
* Purpose:  Decimal to Binary convert
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""

import re
from Algorithm_Programs.utility import algorithm
ref = algorithm


inps = input("Enter the Decimal")

cheack = re.search(r"^[\d]+$",inps)

if cheack:
    inps = int(inps)
    print(ref.dec_to_binary(inps))

else:
    print("Wrong input")



