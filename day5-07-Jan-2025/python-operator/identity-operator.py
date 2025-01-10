"""
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal,
 but if they are actually the same object, with the same memory location:

 is 	   Returns True if both variables are the same object       e.g x is y
 is not	 Returns True if both variables are not the same object   e.g	x is not y
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(" is 	   Returns True if both variables are the same object       e.g x is y")
print(x is z) # return true because x is the same object as z 
print(y is z) # return false because y is not the same object as z
print(x is y) #returns False because x is not the same object as y, even if they have the same content

print(x == y) #to demonstrate the difference betweeen "is" and "==": 
              #this comparison returns True because x is equal to y
print("\n")
print("is not	 Returns True if both variables are not the same object   e.g	x is not y ")
#is not
print(x is not z) # return false because x is the same object as z
print(y is not x) # return tru because y is not same object as y, even they have the same content

print(x != y) # to demonstrate the difference betweeen "is not" and "!=": 
              #this comparison returns False because x is equal to y