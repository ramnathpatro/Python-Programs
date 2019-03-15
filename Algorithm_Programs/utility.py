

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
    def remove_space(str):
        temp = ""
        for char in str:
            if char != " ":
                temp += char

        return temp

    def conv_low_case(str):
        temp = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                char = ord(char) + 32
                temp += chr(char)
            else:
                temp += char

        return temp

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

    def countCurrency(amount):
        notes = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        print("Currency Count -> ")
        for note, no_of_note in zip(notes, noteCounter):
            if amount >= note:
                no_of_note = amount // note
                amount = amount - no_of_note * note
                print(note, " : ", no_of_note)

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
        return "Day Of The Week :", weeks[d], months[month], year

    def Celsius_to_Fahrenheit():
        c = input("Enter the Celsius temp")
        cheack = re.search(r"^[\d]+|[\d]+\.[\d]+$", c)
        if cheack:
            c = float(c)
            f = (c * 9 / 5) + 32
            return f
        else:
            print("Enter digit only")

    def Fahrenheit_to_Celsius():
        f = input("Enter the Fahrenheit temp")
        cheack = re.search(r"^[\d]+|[\d]+\.[\d]+$", f)
        if cheack:
            f = float(f)
        c = (f - 32) * 5 / 9
        return c

    def payment(P, Y, R):
        r = R / (12 * 100)
        n = 12 * Y
        pay = P * r / (1 - pow((1 + r), (-n)))
        return pay

    def dec_to_binary(inps):
        binary_value = ""
        while inps > 1:
            temp = inps % 2
            binary_value += str(temp)
            inps = inps // 2
        binary_value = str(inps % 2) + binary_value
        return binary_value

    def Newton_sqrt(c_inp):
        epsilon = 1e-15
        t = c_inp
        while math.fabs(t - c_inp / t) > epsilon * t:
            t = ((c_inp / t) + t) / 2
        return t