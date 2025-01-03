"""
This is multiline comment 
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain 
as it was, global and with the original value.
"""
myName = 'Rajeev Kumar'
def myfun():
  myName = 'Rajeev Kumar Singh'
  print("My Name is: ", myName)

myfun()
print("My Name is: ", myName)