'''

it has two pointer head and tail that points to first and last node

'''
# We have to know all advantages of operations
'''
INSERT

Insert from head is O(1)
    Steps:
        1.Point a node to what the head is pointing
        2.Point the head to this new node

Inset from tail is O(1)
    Steps:
        1.Point the last node to the new node
        2.Point the tail to the new node

Insert in between the node is O(n)
    Steps:
        1.iterate throught he list and one u find the node.
        2.save the address of the next node to next address of the new node.
        3.save the new node address to the address of the found node

Removal

Remove from Head is O(1)
    steps:
        1.Point the head to next address of the node 

Remove From Tail is O(n)
    steps:
        1.iterate throgh the entire Linked List to find the address of the Previous node
        2.point the tail to the last but one's node

Remove in between is O(n)
    Steps:
        1.find the node
        2.save the pointer of previous node to next node.
        3.delet the pointer of current node to null

'''
# Linked List VS List:

# Advantage
'''

Prepend O(1) -->O(N) in list
Pop First O(1) -->O(N) in list

'''
# DisAdvantage
'''

Looking up by Index O(1) -->O(N) in Linked List
POP is O(1)-->O(N) in Linked List

'''

#----------------------------------------------------------------------#
'''
Actual immplimentation
'''

head = {
        "value":11,
        "next":{
                "value":12,
                "next":{
                        "value":13,
                        "next": None
                    }
        }
}
print(head["next"]["next"]["value"])