import math
try:
    t = int(input("Enter the temperature"))
    v = int(input("Enter the absolute value, it should be '3' to '120'"))

    if t <= 50 and v >= 3 and v <= 120:
        w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*(v**0.16)
        print("Wind Chill speed is: ",w)
    else:
        print("Enter correct value")

except:
    print("Enter number only")