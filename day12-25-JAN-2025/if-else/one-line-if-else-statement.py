'''
# One line if else statement 
a = 5 
b = 55
print("A") if a>b else print("B")
'''

'''
# Example: One line if else statement, with 3 conditions:

a = 555
b = 555
print("A") if a > b else print("=") if a == b else print("B")

'''

'''
# The and keyword is a logical operator, 
# and is used to combine conditional statements:
# Example: Test if a is greater than b and c is greater than a 
a = 5 
b = 3
c = 55
if a > b and c > a:
  print("Both condition are True")

'''

'''
# Example: Test if a is greater than b, OR if a is greater than c:
a = 55
b = 5
c = 555
if a > b or a > c:
  print("At least one of the condition is True")
'''


# Example: Test if a is NOT greater than b:
a = 5
b = 55
if not a > b: 
  print("a is NOT greater than b")

  