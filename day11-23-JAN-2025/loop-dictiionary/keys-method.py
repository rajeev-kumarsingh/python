# You can use the keys() method to return the keys of a dictionary:

loopExample = {
  "using": "for loop",
  "return values are": "key of the dictionary",
  "syntax": "for x in loopExample",
  "print": "print(loopExample)",
  "test": "number of times print"
}
# Use keys() method to return keys of a dictionary
print("use keys() method to get keys: 'for x in loopExample.keys(): print(x)' ")
for x in loopExample.keys():
  # Print all keys in the dictionary, One by One
  print("Keys in the dictionary: ", x)

print("\n")

print("Another way to get keys: use: 'for x in loopExample: print(x)'")

# Another way to get the keys
for x in loopExample:
  # Print all keys in the dictionary, One by One
  print("Keys in the dictionary: ",x)
  # Print all values in the dictionary, One by One
  # Print all values in the dictionary, One by One
  #print("Values in the dictionary: ", loopExample[x])
  