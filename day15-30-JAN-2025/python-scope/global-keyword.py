'''
# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, 
# you can use the global keyword.

# The global keyword makes the variable global.
'''
# If you use the global keyword, the variable belongs to the global scope:

'''
def myFun():
  global x 
  x = 500
  print("From myFun: ",x)
myFun()
print("From outside of function: ", x)
'''
x = 5500
def myFun():
  global x 
  x = 5000
  print("From myFun: ",x)
myFun()
print("From outside of function: ", x)
