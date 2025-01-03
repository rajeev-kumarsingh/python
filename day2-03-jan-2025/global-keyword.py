"""
This is multiline comment 
Normally, when you create a variable inside a function, that variable is local, and can only
 be used inside that function.

To create a global variable inside a function, you can use the global keyword.
If you use the global keyword, the variable belongs to the global scope:

"""
def myfun():
  global myName
  myName = "Rajeev Kumar Singh"
  #print("My Name is: ", myName)

myfun()
print("My Name is: ", myName)