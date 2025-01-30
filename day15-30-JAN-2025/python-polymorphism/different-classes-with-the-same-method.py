# Different classes with the same method
class car:
  def __init__(self,brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive")

class boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail")

class plain:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("fly")
carObject = car("Ford", "Mustang")  # Create car object
boatObject = boat("Ibiza", "Touring 20") # Create boat object
plainObject = plain("Air India", 747) # Create plain Object

for x in (carObject, boatObject, plainObject):
  x.move()
