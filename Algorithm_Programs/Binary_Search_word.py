
"""
******************************************************************************
* Purpose:  Binary Search the Word from Word List
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
******************************************************************************
"""

from Algorithm_Programs.utility import algorithm
ref = algorithm #ref is reference

# Binary Search the Word from string

def binary_search_word():
    inps = input("Enter the String")  #user input form keybord
    sear = input("what you want to search")  #user input form keybord, what he want to search in the above string
    str_word = ref.create_str_to_word(inps)  #Here string is convert word, calling function and argument
    sort_word = ref.bubble_sort(str_word) #here word are sorted, calling function and argument
    if ref.binary_search(sort_word, sear): # here chacking the condition
        print(sear, "is a index of ", ref.binary_search(sort_word, sear)) # print the reselt
    else:
        print(sear, "Not Found")

# main function is called

if __name__ == '__main__':
    binary_search_word()

