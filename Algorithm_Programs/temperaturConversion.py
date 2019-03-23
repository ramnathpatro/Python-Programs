

"""
******************************************************************************
* Purpose:  Fahrenheit_to_Celsius and Celsius_to_Fahrenheit
* @author:  Ramnath Patro
* @version: 1.0
* @since:   13-3-2019
*
******************************************************************************
"""


import re
from Algorithm_Programs.utility import algorithm
ref = algorithm

def temp_Conversion():
    while True:
        print("1.Fahrenheit_to_Celsius")
        print("2.Celsius_to_Fahrenheit")
        print("3.Exit")
        print()

        option = input("Enter the Option")

        cheack = re.search(r"^[\d]+$", option)

        if cheack:
            option = int(option) # convert str to int
            if option == 1:
                print(ref.Fahrenheit_to_Celsius())

            elif option == 2:
                print(ref.Celsius_to_Fahrenheit())

            elif option == 3:
                print("Exit")
                exit()
            else:
                print("Invalid input")

        else:
            print("Enter valid number only")
            print()


if __name__ == '__main__':
    temp_Conversion()



