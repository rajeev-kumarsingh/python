'''
for loops cannot be empty, 
but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.

'''
'''

for i in [0,2,3,4,65]:
  pass
print("\n")
myName = "Rajeev Kumar Singh"
for i in myName:
  pass
myAddr = {
  "city": "Bangalore",
  "location": "BTM",
  "pin-code": 560076
}
for i in myAddr:
  pass
'''

myAddr = {
  "city": "Bangalore",
  "location": "BTM",
  "pin-code": 560076
}
for i in myAddr:
  #pass