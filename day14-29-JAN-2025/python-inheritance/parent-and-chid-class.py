# Create a Parent class 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print( f" Hello everyone my firstname is '{self.firstname}' and my lastname is '{self.lastname}'" )
  
  def printnamechild(self):
    print( f" Hello everyone,I am from child class and  my firstname is '{self.firstname}' and my lastname is '{self.lastname}'" )
# Use the Person class to create an object, and then execute the printname method
parentobject1 = Person("Rajeev", "Singh")
parentobject1.printname()


# Create a child class 
# Create a class named Student, which will inherit the properties and methods from the Person class:
class student(Person):
  pass

# Use the Student class to create an object, and then execute the printname method:
childobject = student("Bittu", "Kumar")
childobject.printnamechild()
