

"""
******************************************************************************
* Purpose:  Vending machine which can be returned minimum number of Notes
* @author:  Ramnath Patro
* @version: 1.0
* @since:   14-3-2019
*
******************************************************************************
"""




import re
from Algorithm_Programs.utility import algorithm
ref = algorithm


strs = [1,5,6,4,3,2,8,9,78]
#str = input("Enter the string")

def dayofweek(d, m, y):
    t = [0, 3, 2, 5, 0, 3,
         5, 1, 4, 6, 2, 4]
    y -= m < 3
    return ((y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)


# Driver Code
day = dayofweek(14, 3, 2019)
print(day)


























"""
for i in range(len(strs)):
    i = str(strs[i])
    print(type(i))

prime_anagram = []
inp = input("Enter number only")
check_int = re.search(r"^[\d]+$", inp)
if check_int:
    inp = int(inp)
    prinm_num = ref.prime_number(inp)
    print(prinm_num)
    for num1 in range(len(prinm_num)):
        for num2 in range(num1+1, len(prinm_num)-1):
            num = str(prinm_num[num1])



def create_str_to_word(inps):
    list_word = [] #empty list
    temp = "" #empty string
    for i in inps:
        if i == " ":
            list_word.append(temp)
            temp = ""
        else:
            temp += i
    list_word.append(temp)
    return list_word

print(create_str_to_word(inps))


"""















"""
str = list(str)



temp = ""
for char_f in range(len(str)-1):

    for char_S in range(char_f +1, len(str)):
        if str[char_f] > str[char_S]:
            print(str[char_f],"----",str[char_S])
            temp = str[char_f]
            str[char_f] = str[char_S]
            str[char_S] = temp

print(str)
"""


