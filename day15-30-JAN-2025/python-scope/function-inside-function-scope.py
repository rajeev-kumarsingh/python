'''
# Function inside function
# the variable x is not available outside the function, 
# but it is available for any function inside the function:
'''
def myFun():
  x = 500
  print("From myFun: ",x)
  def myInnerFun():
    print("From myInnerFun: ", x)
  myInnerFun()

myFun()