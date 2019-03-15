
def inser_sort(slist):
    for i in range(1 ,len(slist)):
        key = slist[i]
        j = i - 1
        while j >= 0 and key < slist[j]:
            slist[ j +1] = slist[j]
            j -= 1
        slist[ j +1] = key
    print(slist)


def binary_search(a ,sear):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if sear == a[mid]:
            return True
        elif sear < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def bubble_sort(a):
    temp = ""
    for i in range(len(a ) -1):
        for j in range( i +1 ,len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a



t = ""
a = []
# sear = "is"
inp = input("enter the String")
# sear = input("Find the word")

for i in inp:
    if i == " ":
        a = a + [t]
        t = ""
    else:
        t+=i
a = a + [t]


while True:
    print("1.Bubble Sort")
    print("2.Inser Sort")
    print("3. Binary Search")

    option = int(input("Enter the option"))

    if option == 1:
        print(bubble_sort(a))
    elif option == 2:
        inser_sort(a)
    elif option == 3:
        sear = input("Search the element")
        sorts = bubble_sort(a)
        # sorts = ["is" , "my" , "room" , "this"]

        binary_search(sorts,sear)
        if binary_search(sorts,sear):
            print("Found")
        else:
            print("Not Found")
    elif option == 4:
        print("Exit")
        break
    else:
        print("Wrong Option")

















