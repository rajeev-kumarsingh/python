'''
Let us create a method in the Person class:

Insert a function that prints a greeting, and execute it on the p1 object:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def my_fun(self):
    print("Hello my name is ", self.name)
p1 =Person("Rajeev Kumar Singh", 32)
p1.my_fun()
