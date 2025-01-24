#The popitem() method removes the last inserted item (in versions before 3.7, 
# a random item is removed instead):

car = {
  "Name": "Ford",
  "Model": "Mustang",
  "Year": 1964
}
print(car)
car.popitem()
print("after apply popitem(): ", car)
