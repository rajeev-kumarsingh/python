
'''
Another way to make a copy is to use the built-in function dict().

Example
'''
dict1 = {
  "dict1key1": "dict1value1",
  "dict1key2": "dict1value2",
  
}
dict2 = {
  "dict2key1": "dict2value1",
  "dict2key2": "dict2value2",
  
}
print("dict1: ", dict1)
print("dict2: ", dict2)
#myDict = dict1.copy()
#myDict1 = dict2.copy()
# Use dict() method to copy dictionary
mydict1 = dict(dict1)
mydict2 = dict(dict2)
print("mydict1: ", mydict1)
print("mydict2", mydict2)
