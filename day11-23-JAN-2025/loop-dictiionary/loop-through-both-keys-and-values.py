# Loop through both keys and values, by using the items() method:

loopExample = {
  "using": "for loop",
  "return values are": "key of the dictionary",
  "syntax": "for x in loopExample",
  "print": "print(loopExample)",
  "test": "number of times print"
}
# Using items() method, loop through both keys and values
for x,y in loopExample.items():
  print(x,":",y)
