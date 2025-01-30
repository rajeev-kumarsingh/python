'''
# Inheritance class Polymorphism
# Create parent class called Vehicle, 
#  and make Car, Boat, Plane child classes of Vehicle,
#  the child classes inherits the Vehicle methods, but can override them:
'''
class vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class car(vehicle): # child class car
  pass
class boat(vehicle): # child class boat
  def move(self):
    print("Sail")
    #return super().move()

class plain(vehicle): # child class plain
  def move(self):
    print("Fly")
    #return super().move()
carObject = car("BMW", "BMW XM") # Create car object
boatObject = boat("GAMEFISH 28CB", "Sea Hunt Gamefish 28:") # Create boat object
plainObject = plain("Boeing 777", "Boeing 777X")

for x in (carObject, boatObject, plainObject):
  print(x.brand)
  print(x.model)
  x.move()