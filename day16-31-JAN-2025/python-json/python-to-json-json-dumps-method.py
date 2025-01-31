# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# Convert from Python to JSON:
import json

'''

# a python object dictionary
details = {
  "fname": "Rajeev",
  "mname": "Kumar",
  "lname": "Singh", 
  "age": 30,
  "car": "Audi"
}
print(type(details))
x = json.dumps(details)
print(x)
print(type(x))

print("\n")
'''
## Convert from Python to JSON
'''

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''
''' 
tupleDetails = json.dumps(("Rajeev", "Kumar", "Singh"))
listDetails = json.dumps(["Rajeev", "Kumar", "Singh"])
stringDetails = json.dumps("Rajeev")
integerDetails = json.dumps(55)
floatDetails = json.dumps(55.55)
boolDetails = json.dumps(True)
boolDetailsFalse = json.dumps(False)
noneTypeDetails = json.dumps(None)

print('json.dumps(("Rajeev", "Kumar", "Singh"))', tupleDetails)
print(type(tupleDetails))
print('json.dumps(["Rajeev", "Kumar", "Singh"])', listDetails)
print(type(listDetails))
print('json.dumps("Rajeev") ', stringDetails )
print(type(stringDetails))
print('json.dumps(55) ', integerDetails)
print(type(integerDetails))
print('json.dumps(55.55) ', floatDetails)
print(type(floatDetails))
print('json.dumps(True) ', boolDetails)
print(type(boolDetails))
print('json.dumps(False) ', boolDetailsFalse)
print(type(boolDetailsFalse))
print('json.dumps(None) ', noneTypeDetails)
print(type(noneTypeDetails))
'''

# Convert a Python object containing all the legal data types:
'''

x = {
  "name": "Rajeev",
  "age": 30,
  "employed": True,
  "married": False,
  "books": ("Linux","javascript"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x)
print(type(y))
print(y)
'''

'''
x = {
  "name": "Rajeev",
  "age": 30,
  "employed": True,
  "married": False,
  "books": ("Linux","javascript"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x, indent=4 )
print(type(y))
print(y)
'''



x = {
  "name": "Rajeev",
  "age": 30,
  "employed": True,
  "married": False,
  "books": ("Linux","javascript"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x, indent=4, separators=(". ", " = ") )
print(type(y))
print(y)


