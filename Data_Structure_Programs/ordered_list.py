file_read = open("test_number.txt", "r")
numbers = file_read.read()
file_read.close()
print(type(numbers))

numbers = numbers.strip().split()
lit_num = []
for num in numbers:
    lit_num.append(int(num))

print(lit_num)