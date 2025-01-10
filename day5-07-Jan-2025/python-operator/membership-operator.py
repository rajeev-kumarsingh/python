"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:
"""
print("Membership operators are used to test if a sequence is presented in an object")
x = ["apple", "grapes"]
print("apple" in x) # returns True because a sequence with the value "apple" is in the list
print("apple" not in x) # # returns false because a sequence with the value "banana" is in the list

print("\n")
print("banana" in x) # returns false because a sequence with the value "banana" is not in the list
print("banana" not in x) # returns True because a sequence with the value "banana" is not in the list
