
"""
******************************************************************************
* Purpose:  Create Utility Class having following static methods
*              i.binarySearch method for integer
*              ii.binarySearch method for String
*              iii.insertionSort method for integer
*              iv.insertionSort method for String
*              v.bubbleSort method for integer
*              vi.bubbleSort method for String
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
******************************************************************************
"""

import re
from Algorithm_Programs.utility import algorithm

ref = algorithm


def search_sort():
    while True:
        print("1.binarySearch method for integer")
        print("2.binarySearch method for String")
        print("3.insertionSort method for integer")
        print("4.insertionSort method for String")
        print("5.bubbleSort method for integer")
        print("6.bubbleSort method for String")
        print("7.Exit the program\n")
        option = int(input("Enter the option"))

        # binarySearch method for integer
        if option == 1:
            total_ele = input("how much element you have to input")
            cheack = re.search(r"^[\d]+$", total_ele)  # cheack it is int or not
            if cheack:
                total_ele = int(total_ele) # convert str to int
                ele = ref.inser_int(total_ele) # convert str to int
                sort_list = ref.bubble_sort(ele) # convert str to int
                sear = int(input("search the integer"))
                if ref.binary_search(sort_list, sear):
                    print(ref.binary_search(sort_list, sear))
                else:
                    print("Not found")
            else:
                print("Enter number only")


        elif option == 2:
            inps = input("Enter the string")
            sear = input("search the char")
            inps = ref.bubble_sort(inps)
            if ref.binary_search(inps, sear):
                print(sear, " index of ", ref.binary_search(inps, sear), )
            else:
                print("Not found", sear)


        elif option == 3:
            total_ele = input("how much element you have to input")
            cheack = re.search(r"^[\d]+$", total_ele)
            if cheack:
                total_ele = int(total_ele)
                ele = ref.inser_int(total_ele)
                print(ref.inser_sort(ele))
            else:
                print("Enter number only")


        elif option == 4:
            inps = input("Enter the string")
            print(ref.inser_sort(inps))


        elif option == 5:
            total_ele = input("how much element you have to input")
            cheack = re.search(r"^[\d]+$", total_ele)
            if cheack:
                total_ele = int(total_ele)
                ele = ref.inser_int(total_ele)
                print(ref.bubble_sort(ele))
            else:
                print("Enter number only")

        elif option == 6:
            inps = input("Enter the string")
            print(ref.bubble_sort(inps))


        elif option == 7:
            print("Exit")
            exit()

        else:
            print("Worng option")

if __name__ == '__main__':
    search_sort()
