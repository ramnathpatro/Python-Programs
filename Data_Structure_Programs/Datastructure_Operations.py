from Data_Structure_Programs.Node_class import Node


class linkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self.top = None
        self.front = None
        self.rear = None
        self.stack_Array = []

    """++++++++++++++++++++++++++++++add the node in linked list++++++++++++++++++++++++++++"""

    def add(self, data):
        new_Node = Node(data)

        if self.size == 0:
            self.first = new_Node
            self.last = new_Node
        else:
            self.last.next = new_Node
            self.last = new_Node
        self.size += 1

    def search(self, ser_word):
        temp = self.first
        while temp is not None:
            if temp.data == ser_word:
                print(ser_word, "is Found")
                # return ser_word
            # else:
            #     print(ser_word, "Not in the list")

            temp = temp.next
        # return None

    def sizeOf(self):
        print("size of list is ", self.size)

    def isEmpty(self):
        if self.size == 0:
            print("List is Empty")

        else:
            print("List contain ", self.size, "of Element")

    def display(self):
        my_list = []
        temp = self.first

        while temp is not None:
            my_list.append(temp.data)
            temp = temp.next
        return my_list

    def remove(self, item):
        temp = self.first
        prev = None
        if temp.data == item:
            self.first = temp.next
            self.size -= 1
            return True
        else:
            while temp:
                if temp.data == item:
                    prev.next = temp.next
                    temp.next = None
                    return True

                else:
                    prev = temp
                    temp = temp.next
            self.size -= 1

    def insert(self, data, pos):
        temp = self.first
        prev = None
        new_Node = Node(data)
        if pos > 0 or pos < self.size:
            for node_no in range(self.size):
                if i == pos:
                    self.size += 1
                    new_Node.next = temp
                    prev.next = new_Node
                    break
                else:
                    prev = temp
                    temp = temp.next


    def orderedAdd(self,data):
        new_node = Node(data)
        temp = self.first
        if self.size == 0:
            self.first = new_node
        else:
            while temp is not None:
                pass


    """+++++++++++++++++++++++Simple Balanced Parentheses+++++++++++++++++++++++++++++"""

    def push(self,data):
        self.stack_Array.append(data)


    def pop(self):

        try:
            return self.stack_Array.pop()
        except:
            print("stack is Empty can not pop")

    def size(self):
        return len(self.stack_Array)

    def isEmpty(self,stack):
        return stack == []

    def print_stack(self):
        for num in self.stack_Array:
            print(num,end="")






class Dequeue:

    def __init__(self,capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.dequeue = []*capacity

    def insert_at_rear(self,data):
        if self.capacity == self.rear:
            print("Dequeue is full")
        else:
            for deq_data in data:
                self.dequeue.append(deq_data)
                self.rear+= 1

    def display(self):
        if self.front == self.rear:
            print("Empty dequeue")
        else:
            for deq_data in range(self.rear):
                print(self.dequeue[deq_data],"  ", end="")
                self.dequeue.append(deq_data)
                self.rear-=1

    def remove_from_front(self):
        if self.front == self.rear:
            print("Empty dequeue")
        else:
            self.front += 1
            return self.dequeue[self.front - 1]

    def remove_from_rear(self):
        if self.rear == self.front:
            print("Empty deququq")
        else:
            self.rear-= 1
            return self.dequeue[self.rear]













