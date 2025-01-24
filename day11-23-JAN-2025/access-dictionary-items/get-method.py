
address = dict(name = "Rajeev", age = 32, profession = "DevOps")
print(address)
print(type(address))
print(len(address))
print(address["name"])
print(address["age"])
print(address["profession"])


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

