'''

To test if we make assign address or value


'''
num1 = 10
num2 = num1
print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)
print("num1 is pointing to :",id(num1))
print("num2 is pointing to :",id(num2))
# what  will happen if we update the value of num2 to 12
num2 = 12
print("num1 =", num1)
print("num2 =", num2)
print("num1 is pointing to :",id(num1))
print("num2 is pointing to :",id(num2))

''' the address is updated Not what Int is immutable so its saving in other location'''
#---------------------------------------------------------------------------------------------------------------------#
'''

But Dictionary are mutable so it would change in both place if we update one place.

'''
dict1 = {"value":11}
dict2 = dict1
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict1 is pointing to :",id(dict1))
print("dict2 is pointing to :",id(dict2))
dict2['value'] = 22
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict1 is pointing to :",id(dict1))
print("dict2 is pointing to :",id(dict2))

# if nothing is carring the address of the dictionary then we will be uping it to garbage collectors