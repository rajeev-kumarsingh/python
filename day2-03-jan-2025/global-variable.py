"""
This is multiline comment 
* Variable that are created outside of a function is known as global variable
* Global variable can be used by everyone, both inside of funtion and outside
"""
x = 'Rajeev Kumar'
def myfun():
  y = 'Singh'
  print("My First name is: ", x)
  print("My Last name is: ", y)

myfun()
print(myfun)
print(type(myfun))
print(type(x))


