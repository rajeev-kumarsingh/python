'''

# Local Scope
A variable created inside a function belongs to the local scope of that function,
 and can only be used inside that function.

'''
def myFun():
  x = 500
  print("From Inside the frunction printing the values of x: ",x)

myFun()
print("From outside the function printing the values of x",x)
