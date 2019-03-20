from Data_Structure_Programs.Datastructure_Operations import linkedList

sep_word=[]
li = linkedList()
file_r = open("test.txt", "r")
sep_word = file_r.read()
#print(sep_word)
data = sep_word.strip().split()
file_r.close()
for i in data:
    li.add(i)

#print(sep_word)
ser_word1 = input("Search the word")
li.search(ser_word1)
a = []
if ser_word1 in sep_word:
    result = li.remove(ser_word1)
    a = li.display()
    print("Element is found")
else:
    li.add(ser_word1)
    a = li.display()
    print("Element not found")
temp = ""
print(a)

print(">>>",temp)
temp = " ".join(a)
print(temp)
print(type(temp))

fw = open("test.txt", "w")
fw.write(temp)
print("File Execution is complete")


fw.close()




