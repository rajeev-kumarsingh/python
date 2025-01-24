# The del keyword removes the item with the specified key name:
car = {
  "Name": "Ford",
  "Model": "Mustang",
  "Year": 1964
}
print(car)
# Delete "Model" key and its value
del car["Model"]
print("After applying del to delete 'Model' item with it's value: ",car)

# delete the dictionary
del car
print(car)
