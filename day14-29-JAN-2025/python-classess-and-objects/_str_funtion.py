'''
# _str_ function
The __str__() function controls what should be returned when the class object is represented
 as a string.

'''

#If the __str__() function is not set, the string representation of the object is returned:
# Example: The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Rajeev", 32)
print(p1)

print("\n")

# Example: The string representation of an object WITH the __str__() function:
class Person1:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return f" Name: {self.name}, and age is: {self.age}"
p2 = Person1("Singh", 31)
print(p2)