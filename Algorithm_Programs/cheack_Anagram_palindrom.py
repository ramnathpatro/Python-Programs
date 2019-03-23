
"""
******************************************************************************
* Purpose:  Cheack the prime number is Anagram or Palindrom
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""


import re
from Algorithm_Programs.utility import algorithm
ref = algorithm
def prime_anagram_Palindrome_cheack():
    inp = input("Enter number only")
    check_int = re.search(r"^[\d]+$", inp)
    if check_int:
        inp = int(inp) # convert str to int
        print("prime_anagram number is:-",ref.cheack_prime_Anagram(inp))
        print("+++++++++++++++++++++++++++++++++")
        print("prime_Palindrome is :-",ref.prime_Palindrome(inp))
    else:
        print("Enter number only not String")

if __name__ == '__main__':
    prime_anagram_Palindrome_cheack()