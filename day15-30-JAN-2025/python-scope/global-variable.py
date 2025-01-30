'''
# Global Variable
# A variable created in the main body of the Python code is a global variable and 
# belongs to the global scope.
# Global variables are available from within any scope, global and local.
'''
x = 500
def myFun():
  print("From myFun accessing gloabal variable x: ", x)
  def myInnerFun():
    print("From myInnerFun accessing global variable x: ", x)
  myInnerFun()
myFun()
print("From Outside of function printing global variable x: ", x)
