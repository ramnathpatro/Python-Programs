from Algorithm_Programs.utility import algorithm
ref = algorithm
import numpy

inp = int(input("Enter the range"))
lis = ref.prime_number(inp)

#print("lis print",lis)
array = numpy.zeros((10,168))
#print(array)

for i in range(len(lis)):
    #print(lis[i])
    if lis[i] < 100:
        array[0][i] = lis[i]

for i in array[0]:
    if i == 0:
        continue
    print(int(i), end=" ")


print()
for i in range(len(lis)):
    #print(lis[i])
    if lis[i] < 200 and lis[i]>101:
        array[1][i] = lis[i]

for i in array[1]:
    if i == 0:
        continue
    print(int(i), end=" ")

print()

for i in range(len(lis)):
    #print(lis[i])
    if lis[i] < 300 and lis[i]>201:
        array[2][i] = lis[i]

for i in array[2]:
    if i == 0:
        continue
    print(int(i), end=" ")

print()

for i in range(len(lis)):
    #print(lis[i])
    if lis[i] < 400 and lis[i]>301:
        array[3][i] = lis[i]

for i in array[3]:
    if i == 0:
        continue
    print(int(i), end=" ")


