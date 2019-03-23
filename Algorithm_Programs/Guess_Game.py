

"""
******************************************************************************
* Purpose:  guess_number
* @author:  Ramnath Patro
* @version: 1.0
* @since:   15-3-2019
*
******************************************************************************
"""

from Algorithm_Programs.utility import algorithm
ref = algorithm

if __name__ == '__main__':

    try:
        lowerNumber = int(input("Enter lower Bound :"))
        highNumber = int(input("Enter higher Bound  :"))
        reult = ref.Guess_Game(lowerNumber, highNumber)
        print(reult)
    except ValueError:
        print("Invalid Input ! Plz entered the valid input")




