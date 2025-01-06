"""
Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,
"""

print(bool("hello")) # True
print(bool(5)) # True

#evaluate 2 values 
x = "Rajeev"
y = 55
print(bool(x)) # True
print(bool(y)) # True

print(bool(0))        # False (0 is falsy)
print(bool(1))        # True (1 is truthy)
print(bool(""))       # False (empty string is falsy)
print(bool("Hello"))  # True (non-empty string is truthy)
print(bool(None))     # False (None is falsy)

print(bool([]))       # False (empty list is falsy)
print(bool([1, 2, 3]))  # True (non-empty list is truthy)
print(bool({}))       # False (empty dictionary is falsy)
print(bool({"key": "value"}))  # True (non-empty dictionary is truthy)
