
intg_lists = [5,-5,10,-8,2,-2,10,11]
zero_int = []
out = []
x = False
for in1 in range(len(intg_lists)-2):
    for in2 in range(1, len(intg_lists)-1):
        for in3 in range(2,len(intg_lists)):
            if intg_lists[in1] + intg_lists[in2] + intg_lists[in3] == 0:
                zero_int.append(intg_lists[in1])
                zero_int.append(intg_lists[in2])
                zero_int.append(intg_lists[in3])
                x = True


            if x == True and len(zero_int) != 0:
                out.append(zero_int)
                zero_int = []

print(out)


