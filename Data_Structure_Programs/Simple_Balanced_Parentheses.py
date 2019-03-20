from Data_Structure_Programs.Datastructure_Operations import linkedList
li = linkedList()
expression = []
expression = input("Enter the Expression")

while len(expression) == 0:
    print("Please Enter Arithmetic Expression")
    expression = input()

if expression[0] == ")" or expression[0] == "}" or expression[0] == "]":
    print("Arithmetic Expression not balanced")
else:
    st1 = []
    res = ""
    #print(">>",st1)
    for i in range(len(expression)):
        if expression[i] == "(" or expression[i] == "{" or expression[i] == "[":
            st1 = li.push(expression[i])
            #print("+++",st1)

        elif expression[i] == ")":
            res = li.pop()
            print(res)
            if res != "(":
                print("aa","Arithmetic Expression is not balanced")
                exit()

        elif expression[i] == "}":
            res = li.pop()
            if res !="{":
                print("bb","Arithmetic Expression is not balanced")
                exit()

        elif expression[i] == "]":
            res = li.pop()
            if res !="[":
                print("bb","Arithmetic Expression is not balanced")
                exit()
    """         
    if "(" not in st1 and "{" not in st1 and "[" not in st1:
        print("Arithmetic Expression is balanced")
    else:
        print("Arithmetic Expression is not balanced")
    """
    if li.isEmpty(li.stack_Array):
        print("Arithmetic Expression is balanced")
    else:
        print("Arithmetic Expression is not balanced")



# li.isEmpty(li.stack_Array)