
"""
******************************************************************************
* Purpose:  Anagram
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""


from Algorithm_Programs.utility import algorithm
reff = algorithm

def anagram():
    str1 = input("Enter the 1st String")
    str2 = input("Enter the 2nd String")
    reff.anagram_final(str1,str2)
if __name__ == '__main__':
    anagram()
