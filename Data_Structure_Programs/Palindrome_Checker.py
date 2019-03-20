from Data_Structure_Programs.Datastructure_Operations import Dequeue
de = Dequeue

inps = input("Enter the string for palindrome check")
low_inp = inps.lower()
# print(low_inp)

d = de(len(low_inp))

d.insert_at_rear(low_inp)

# d.display()

for data_num in range(len(low_inp)//2):
    if d.remove_from_front() == d.remove_from_rear():
        if data_num == (len(low_inp)//2)-1:
            print("palindrame")
    else:
        print("Not palindrome")
        break