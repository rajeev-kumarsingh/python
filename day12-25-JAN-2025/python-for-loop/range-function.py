'''
# Using the range() function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, 
 and increments by 1 (by default), and ends at a specified number.

'''
'''
# Basic example
for i in range(6):
  print(i)
'''
'''
# Specifying a Start and Stop
for i in range(2, 8):
  print(i)
'''

'''
# Specifying a Step
for i in range(1,10,4):
  print(i)
'''
'''
# Reverse Sequence
for i in range(10, 0, -2):
  print(i)
'''

'''

# Converting to a List
number = list(range(5))
print(number)
print("\n")
#  Specifying a Start and Stop
number = list(range(0,10))
print(number)
print("\n")
# Specifying a Step
number = list(range(0,10,2))
print(number)
print("\n")
# Reverse Sequence
number = list(range(20,0,-4))
print("Reverse sequence: ",number)
print("\n")
number = list(range(20,-10,-4))
print("Reverse sequence: ",number)
'''

'''

## Common Use Cases
## 1. Iterating in Loops:
for i in range(3):
  print(f"iteration {i}")
'''
'''
# 2. Generating index for list
list1 = ["item1", "item2", "item3", "item4", "item4"]
for index in range(len(list1)):
  print(f"Index-{index} : {list1[index]}")
'''
'''
'''
# Creating ranges of numbers
even = list(range(2,24,2))
print("Even number list between 2 to 24: ",even)
print(type(even))
print("\n")
odd = list(range(1,24,2))
print("Odd number list between 1 to 24: ",odd)
print(type(odd))
