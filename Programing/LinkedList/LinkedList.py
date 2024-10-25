'''

node is a basic class used in an Linked List

LinkedList has the Fucntions below this is want is done:

class Linkedlist:
    __init__ : will initials the Linked List
    Append : will create a node and insert from tail
    Prepend: will create a node and insert from the head
    Insert: will create a node and will insert in the given index

'''

class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.Length = 1
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        newNode = Node(value)
        # add a test case where Head is null
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.Length += 1
        return True
    
    def pop(self):
        if self.Length == 0:
            return None
        temp = self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next =None
        self.Length -=1
        if self.Length == 0:
            self.head=None
            self.tail=None
        return temp.value
            
            



my_linkedList = LinkedList(4)
print(my_linkedList.head.value)

# Print fucntion to print everything in the linked list
my_linkedList.printList()
print("---------Append-------------")
# Append Function 
my_linkedList.append(10)
my_linkedList.append(11)
my_linkedList.append(12)
my_linkedList.printList()

# To check pop function
print("---------pop-------------")
print(my_linkedList.pop())
print("---------Post pop-------------")

my_linkedList.printList()