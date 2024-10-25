'''

This is a way we get to learn if more then one inputs are given in a function other then just n

'''

# example for O(a+b)

def print_items(a,b):
    for i in range(a):
        print(a)
    for j in range(b):
        print(b)

'''

this may seem like O(n)+O(n) => O(2n) => O(n)

But this is wrong we need to undestand its just O(a)+O(b) =>O(a+b)

'''

# example for O(a*b)

def print_item(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

'''
here similarly its not like O(n *n) => O(n^2)

but its simply O(a*b) 
'''