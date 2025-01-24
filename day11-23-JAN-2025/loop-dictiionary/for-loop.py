# You can loop through a dictionary by using a for loop.
# When looping through a dictionary,
#  the return value are the keys of the dictionary

'''
loopExample = {
  "using": "for loop",
  "return values are": "key of the dictionary",
  "syntax": "for x in loopExample",
  "print": "print(loopExample)",
  "test": "number of times print"
}

for x in loopExample:
  print(loopExample)
  

print("\n")
print(type(loopExample))
print(len(loopExample))
print(loopExample.items())
print(loopExample.values())

'''


# Print all key names in the dictionary, one by one:

loopExample = {
  "using": "for loop",
  "return values are": "key of the dictionary",
  "syntax": "for x in loopExample",
  "print": "print(loopExample)",
  "test": "number of times print"
}

for x in loopExample:
  print(x)
  