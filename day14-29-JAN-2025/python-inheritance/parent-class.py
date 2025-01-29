'''
Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:


'''

# Example
# Create a class named Person, with firstname and lastname properties, 
# and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print( f" Hello everyone my firstname is '{self.firstname}' and my lastname is '{self.lastname}'" )

# Use the Person class to create an object, and then execute the printname method
object1 = Person("Rajeev", "Singh")
object1.printname()