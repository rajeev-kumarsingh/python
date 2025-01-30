'''
# nonlocal Keyword
# If you use the nonlocal keyword, the variable will belong to the outer function:
'''
def myFun1():
  x = "Rajeev"
  def fun2():
    nonlocal x
    x = "hello"
  fun2()
  return x
myFun1()
print(myFun1())


  