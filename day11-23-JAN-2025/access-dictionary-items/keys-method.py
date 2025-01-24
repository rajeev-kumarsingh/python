'''
#keys() method return a list of all the keys in the dictionaries




personalDetails ={
"name": "Rajeev Kumar Singh",
"address": {
  "Street": "BTM 2nd Stage",
  "Layout": "BTM",
  "Pin Code": 560076
},
"Phone Number": 6299491504,
"Heigth": 5.11,
"measurement type": "foot and inch"

}

print(len(personalDetails))
print(personalDetails["address"])
print(personalDetails.get("address"))
print(type(personalDetails))
x = personalDetails.keys()
print(x)
'''


'''
The list of the keys is a view of the dictionary, 
meaning that any changes done to the dictionary will be reflected in the keys list.

Example
'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change
print("\n")
print("Length of car dictionary before change is: ",len(car))
print("\n")
car["color"] = "white"
print(x) #after the change
print("\n")
print("car dictionary after added color key and valur white is: ",car)
print("\n")
print("Length of car dictionary after change is:",len(car))
