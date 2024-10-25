my_list = [1,2,3,4,5]



# in adding or removing is first index is O(n) or in any place its O(n) only
my_list.pop(0)
print(my_list)
my_list.insert(0,1)
print(my_list)

# adding or removing in the end is O(1)
my_list.pop()
print(my_list)
my_list.append(6)
print(my_list)

# searching we need 

# search by index is O(1)

# search by value is O(n)