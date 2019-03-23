
"""
******************************************************************************
* Purpose:  To the Util Class add dayOfWeek static function that takes a date
*            as input and prints the day of the week that date falls on. Your
*           program should take three command­line arguments:
*           m (month), d (day), and y (year). For m use 1 for January,
*           2 for February, and so forth. For output print 0 for Sunday,
*           1 for Monday, 2 for Tuesday
*
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""

from Algorithm_Programs.utility import algorithm
ref = algorithm

class day_of_week:
    try:
        m = input("Enter value for Month:")

        while m.isalpha() or int(m) <= 0 and int(m) <= 12:
            m = input("please provide Valid Value(Month)\n")

        d = input("Enter value for Day")

        while d.isalpha() or int(d) <= 0:
            d = input("please provide Valid Value(Month)\n")

        y = input("Enter value for Year:")

        while y.isalpha() or int(y) <= 999:
            y = input("please provide Valid Value(Month)\n")

        print(ref.Day_Of_Week(int(m), int(d), int(y)))

    except ValueError:
        print(">>> Please provid Valid input")


if __name__ == '__main__':
    day_of_week

