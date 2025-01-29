'''
Delete Object

You can delete object by using del keyword

'''
# Create the class and Object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def my_fun(callme):
    print("Hello learners my name is ", callme.name, "and I am ", callme.age)
  def delete(mr):
    print("Hello ", mr.name, "Now I am gonna delete the Object p1 by using del keyword: del p1! ")
# Create Object
p1 = Person("Rajeev Kumar Singh", 30)
p1.my_fun()
# Delete the object p1
p1.delete()
del p1
print(p1)
