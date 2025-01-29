'''
Delete Object Properties
You can delete properties on objects by using the del keyword:

'''


# Create class 
class Person:
  def __init__(forObject, name, age, addr):
    forObject.name = name
    forObject.age = age
    forObject.addr = addr
  def greet(self):
    print("Hello my name is ", self.name, "and I am ", self.age, "I am gonna delete addr properties")
  def delete(self):
    print("Hi", self.name , "addr properties is deleted successfully ")
# Delete the age properties from the p1 object
p1 = Person("Rajeev Kumar Singh", 32, "btm-bangalore")
p1.greet()

# Delete the addr properties from the p1 object
del p1.addr
p1.delete()
print(p1.addr)
