

inp = "Hello <<UserName>>, How are you?"

start = 0
end = 0
x = 0
new_string = ""
proper = 0
while proper < 1:
    name = input("Enter the proper name")
    if len(name) >= 3:
        for char in inp:
            if start == 0 and char != "<":
                new_string += char

            if char == "<" and start == 0:
                new_string += name
                start = 1

            if char == ">":
                end = 1

            if end == 1 and char != ">":
                new_string += char
        proper = 1
   # else:
   #     print("Enter the proper name")




print(new_string)
