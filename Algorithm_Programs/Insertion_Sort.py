
"""
******************************************************************************
* Purpose:  Reads in strings from standard input and prints them in sorted order.
*           Uses insertion sort.
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""

from Algorithm_Programs.utility import algorithm
ref = algorithm


def insettion_sort_word():
    inps = input("Enter the String") #user input form keybord
    str_word = ref.create_str_to_word(inps)  #Here string is convert word, calling function and argument
    sort_word = ref.inser_sort(str_word) #here word are sorted, calling function and argument
    print(sort_word) #print the reselt


if __name__ == '__main__':
    insettion_sort_word()