'''
O(n) is Linear time complexity condition 

example for this is running is single for loop in a fucntion then the fucntion is said to be O(n)
'''

def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# this runs n times that is the size of the given items

# by dorping constant we need to tell only o(n) and not O(2n) => O(n) only