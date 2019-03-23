

"""
******************************************************************************
* Purpose:  Utility class
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""


import math
import re

class algorithm:


    """+++++++++++++++remove space++++++++++++++"""
    def remove_space(str):
        temp = ""
        for char in str:
            if char != " ":
                temp += char

        return temp

    """++++++++++++++convert lower case+++++++++++"""
    def conv_low_case(str):
        temp = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                char = ord(char) + 32
                temp += chr(char)
            else:
                temp += char

        return temp

    """ ++++++++++++++sort the element++++++++++++"""
    def bubble_sort(str):
        str = list(str)
        temp = ""
        for char_f in range(len(str)):
            for char_S in range(char_f + 1, len(str)):
                if str[char_f] > str[char_S]:
                    temp = str[char_f]
                    str[char_f] = str[char_S]
                    str[char_S] = temp

        return str

    """+++++++++++++chack it is Anagrama or not++++++++++++++++"""
    def anagram_final(str1,str2):

        if len(str1) == len(str2):
            str1 = algorithm.remove_space(str1)
            str2 = algorithm.remove_space(str2)
            str1 = algorithm.conv_low_case(str1)
            str2 = algorithm.conv_low_case(str2)
            str1 = algorithm.bubble_sort(str1)
            str2 = algorithm.bubble_sort(str2)
            if str1 == str2:
                print("Anagram")
            else:
                print("Not Anagram")
        else:
            print("Not Anagram")

    """+++++++++++++prime number check++++++++++++++++"""
    def prime_number(upper_range):
        total_num = [num for num in range(upper_range + 1)]
        prime_num = []
        for num in total_num:
            if num > 1:
                for i in range(2, num):
                    if (num % i == 0):
                        break
                else:
                    prime_num.append(num)
        return prime_num
    """++++++++++++prime number Anagram++++++++++++++"""
    def cheack_prime_Anagram(inp):
        prime_anagram = []
        set_prime = []
        prinm_num = algorithm.prime_number(inp)
        for num1 in range(len(prinm_num)):
            for num2 in range(num1 + 1, len(prinm_num) - 1):
                str_num1 = str(prinm_num[num1])
                str_num2 = str(prinm_num[num2])
                if sorted(str_num1) == sorted(str_num2):
                    set_prime.append(str_num1)
                    set_prime.append(str_num2)
                    prime_anagram.append(set_prime)
                    set_prime = []
        return prime_anagram

    """+++++++++++++prime palindrome++++++++++++++"""
    def prime_Palindrome(inp):
        palindrome_list = []
        prime_num = algorithm.prime_number(inp)
        for num in prime_num:
            temp = num
            rev = 0
            while (num > 0):
                dig = num % 10
                rev = rev * 10 + dig
                num = num // 10
            if (temp == rev):
                palindrome_list.append(temp)
        return palindrome_list

    """+++++++++++++++++inser sot for integer+++++++++++++++"""
    def inser_int(total_ele):
        inserded_ele = 0  # constant
        list_ele = []  # empty list
        while inserded_ele < total_ele:
            elements = input("Enter the element")
            cheack_ele = re.search(r"^[\d]+$", elements)  # cheack it is int or not
            if cheack_ele:
                elements = int(elements)
                list_ele.append(elements)
                inserded_ele += 1
            else:
                print("Enter number only")
        return list_ele

    """+++++++++++++++++binary search++++++++++++++++++++++"""
    def binary_search(inps, sear):
        sort_ele = algorithm.bubble_sort(inps)
        low = 0
        high = len(inps) - 1
        while low <= high:
            mid = (low + high) // 2
            if sear == inps[mid]:
                return mid
            elif sear < inps[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False

    """+++++++++++++++++++inser sort+++++++++++++++++"""
    def inser_sort(inps):
        inps = list(inps)
        for i in range(1, len(inps)):
            key = inps[i]
            j = i - 1
            while j >= 0 and key < inps[j]:
                inps[j + 1] = inps[j]
                j -= 1
            inps[j + 1] = key
        return inps

    def create_str_to_word(inps):
        list_word = []  # empty list
        temp = ""  # empty string
        for i in inps:
            if i == " " and temp != "":
                list_word.append(temp)
                temp = ""
            else:
                temp += i
        list_word.append(temp)
        return list_word

    """++++++++++++++++Vending machine+++++++++++++++++"""
    def countCurrency(amount):
        notes = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        print("Currency Count -> ")
        for note, no_of_note in zip(notes, noteCounter):
            if amount >= note:
                no_of_note = amount // note
                amount = amount - no_of_note * note
                print(note, " : ", no_of_note)

    """++++++++++++++cal the day of week+++++++++++++++"""
    def Day_Of_Week(month, day, year):
        months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "April", 5: "May", 6: " Jun", 7: " July", 8: "Aug", 9: "Sept",
                  10: "Oct",
                  11: "Nov", 12: "Dec"}  # dictionary used to store key value pair
        # dictionary used to store key value pair
        weeks = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "San"}
        y = year - (14 - month) // 12
        x = y + y // 4 - y // 100 + y // 400
        m = month + 12 * ((14 - month) // 12) - 2
        d = (day + x + 31 * m // 12) % 7  # calculates weekday
        # print(d)
        return ("Day Of The Week :", weeks[d], months[month], year), d

    """+++++++++++++++Celsius_to_Fahrenheit+++++++++++++++++"""
    def Celsius_to_Fahrenheit():
        c = input("Enter the Celsius temp")
        cheack = re.search(r"^[\d]+|[\d]+\.[\d]+$", c)
        if cheack:
            c = float(c)
            f = (c * 9 / 5) + 32
            return f
        else:
            print("Enter digit only")
    """++++++++++++++Fahrenheit_to_Celsius++++++++++++++++++"""
    def Fahrenheit_to_Celsius():
        f = input("Enter the Fahrenheit temp")
        cheack = re.search(r"^[\d]+|[\d]+\.[\d]+$", f)
        if cheack:
            f = float(f)
        c = (f - 32) * 5 / 9
        return c

    """++++++++++++++++monthly payment+++++++++++++++++++++++"""
    def payment(P, Y, R):
        r = R / (12 * 100)
        n = 12 * Y
        pay = P * r / (1 - pow((1 + r), (-n)))
        return pay
    """++++++++++++++decimal to binary convert++++++++++++++++"""
    def dec_to_binary(inps):
        binary_value = []
        while inps > 1:
            temp = inps % 2
            binary_value.insert(0, temp)
            inps = inps // 2
        binary_value.insert(0, inps % 2)
        return binary_value
    """+++++++++++++++++Newton sqrt++++++++++++++++++++++"""
    def Newton_sqrt(c_inp):
        epsilon = 1e-15
        t = c_inp
        while math.fabs(t - c_inp / t) > epsilon * t:
            t = ((c_inp / t) + t) / 2
        return t

    """+++++++++++++++guess number game++++++++++++++++++"""
    def Guess_Game(lowerNumber, higherNumber):
        print(" Think for Your Secret Number !!")
        first = lowerNumber
        last = higherNumber
        count = 0
        while True:
            mid = (first + last) // 2
            print("Is your secret number %s?" % mid)
            guess = input(
                "Enter h for higher value "
                "Enter l for lower value "
                "Enter c for guessed correctly")
            if guess == 'h':
                first = mid
            elif guess == 'l':
                last = mid
            elif guess == 'c':
                print(' Your secret number was: ' + str(mid))
                break
            else:
                print('TRY AGAIN !! WRONG INPUT.')
            count += 1
        print("Total Number of Guess is : ", count)

        """+++++++++++++++decimal_binary_decimal+++++++++++++++++++++"""
    def decimal_binary_decimal(inps):
        cheack = re.search(r"^[\d]+$", inps)  # chack the it is int or not
        if cheack:
            inps = int(inps)
            if inps <= 255:
                dec_bin = algorithm.dec_to_binary(inps)  # method called
                while len(dec_bin) < 8:
                    dec_bin.insert(0, 0)

                temp = ""
                for bin_num in dec_bin:
                    temp += str(bin_num)
                # swap the binary number
                swap1_4 = temp[:4]
                swap4_8 = temp[4:]
                swap_bin = swap4_8 + swap1_4
                print("Befor swapping:- ", temp)
                print()
                print("After swapping:- ", swap_bin)
                print()
                swap_bin = int(swap_bin)
                # convort binary to decimal
                binary1 = swap_bin
                decimal, inc, = 0, 0,  # constant
                while (swap_bin != 0):
                    dec = swap_bin % 10
                    decimal = decimal + dec * pow(2, inc)
                    swap_bin = swap_bin // 10
                    inc += 1
                print(decimal, type(decimal))
                print("After swapping the decimal NO:- ", decimal)
            else:
                print("Number should be 0 to 255")
        else:
            print("Wrong input")
    """++++++++++++++ merge sort+++++++++++++++++++"""
    def merge_Sort(arr):
        #print("Splitting ", arr)
        if len(arr) > 1:
            mid = len(arr) // 2
            lefthalf = arr[:mid]
            righthalf = arr[mid:]
            algorithm.merge_Sort(lefthalf)
            algorithm.merge_Sort(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    arr[k] = lefthalf[i]
                    i = i + 1
                else:
                    arr[k] = righthalf[j]
                    j = j + 1
                k = k + 1
            while i < len(lefthalf):
                arr[k] = lefthalf[i]
                i = i + 1
                k = k + 1
            while j < len(righthalf):
                arr[k] = righthalf[j]
                j = j + 1
                k = k + 1
        return arr