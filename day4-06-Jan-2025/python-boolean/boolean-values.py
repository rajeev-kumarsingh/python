"""
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
a = 55
b = 555
print("a = 55")
print ("b = 555")
print(a>b)
print(a<b)

if a > b:
  print("a is greater than b")
elif a == b:
  print(" a is equal to b")
else:
  print("a is less than b")
