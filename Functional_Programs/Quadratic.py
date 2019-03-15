import math


try:
    a = int(input("Enter 'a' value"))
    b = int(input("Enter 'b' value"))
    c = int(input("Enter 'c' value"))
    if a < b:
        delta = b * b - 4 * a * c
        root_1_x = (-b +math.sqrt(delta))/(2*a)
        root_2_x = (-b -math.sqrt(delta))/(2*a)

        print("root_1: ",root_1_x,"Root_2: ",root_2_x)
    else:
        print("Enter the correct value ")

except:
    print("Enter Number only")

"""

a = int(input("Enter 'a' value"))
b = int(input("Enter 'b' value"))
c = int(input("Enter 'c' value"))
delta = b * b - 4 * a * c
root_1_x = (-b +math.sqrt(delta))/(2*a)
root_2_x = (-b -math.sqrt(delta))/(2*a)

print("root_1: ",root_1_x,"Root_2: ",root_2_x)
"""