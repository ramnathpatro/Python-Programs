

try:
    inp = input("Enter 4 digit Year only")
    if len(inp) == 4:
        inp = int(inp)
        if inp % 400 == 0 or inp % 4 == 0 and inp % 100 != 0:
            print(inp," is a leap year")
        else:
            print(inp," is not a leap year")
    else:
        print("Enter 4 digit year only")

except:
    print("Enter the 4 digit year only")






