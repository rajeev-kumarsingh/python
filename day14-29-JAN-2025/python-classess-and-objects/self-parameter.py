'''
Self Parameter
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.

It does not have to be named self, 
you can call it whatever you like, 
but it has to be the first parameter of any function in the class:

'''
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age
  def my_fun(abc):
    print("Hell my name is ", abc.name, "and I am ", abc.age)
p1 = Person("Rajeev Kumar Singh", 30)
p1.my_fun()
# Modify Object Properties
p1.age= 28
p1.my_fun()