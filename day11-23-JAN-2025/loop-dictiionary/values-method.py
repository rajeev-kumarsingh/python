# You can also use the values() method to return values of a dictionary:

loopExample = {
  "using": "for loop",
  "return values are": "key of the dictionary",
  "syntax": "for x in loopExample",
  "print": "print(loopExample)",
  "test": "number of times print"
}
# Use values() method to return values of a dictionary
print("use values() method to get values: 'for x in loopExample.values(): print(x)' ")
for x in loopExample.values():
  # Print all values in the dictionary, One by One
  print("Values in the dictionary: ", x)

print("\n")

print("Another way to get values: use: 'for x in loopExample: print(loopExample[x])'")

# Another way to get the values
for x in loopExample:
  # Print all keys in the dictionary, One by One
  #print("Keys in the dictionary: ",x)
  # Print all values in the dictionary, One by One
  # Print all values in the dictionary, One by One
  print("Values in the dictionary: ", loopExample[x])
  