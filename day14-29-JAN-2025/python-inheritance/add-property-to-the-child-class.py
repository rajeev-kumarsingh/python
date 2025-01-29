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
  # Add the __init__() function to the Student class:
  def __init__(self, fname, lname, year):
    '''
    # By using the super() function, you do not have to use the name of the parent element, 
    # it will automatically inherit the methods and properties from its parent.
    # or we can write parent class name instead of super
    # Person.__init__(fname, lname)
    '''
    super().__init__(fname, lname)
    # Add Add a property called graduationyear to the Student class:
    self.graduationyear = year
    #self.graduationyear = 2013
# Use the Student class to create an object, and then execute the printname method:
childobject = student("Bittu", "Kumar", 2013)
childobject.printnamechild()
print(f"Added new property to child class, graduationyear: {childobject.graduationyear}")

