# Example of dictionary
'''
address = {
"name": "Rajeev Kumar Singh",
"phone-number": 6299491504,
"address": "btm 2nd stage",
"city": "bangalore",
"state": "karnataka"
}
print(address)
print(type(address))
'''

'''
# Dictionary items are presented in key:value pairs, 
# and can be referred to by using the key name.

address = {
"myName": "Rajeev Kumar Singh",
"phone-number": 6299491504,
"address": "btm 2nd stage",
"city": "bangalore",
"state": "karnataka"
}
print(address["myName"])
print(address["phone-number"])
print(address["city"])
print(address["state"])
'''

'''
#Dictionaries cannot have two items with the same key:


address = {
"myName": "Rajeev Kumar Singh",
"phone-number": 6299491504,
"address": "btm 2nd stage",
"city": "bangalore",
"state": "karnataka"
#"state": "karnataka"

}
print(address["myName"])
print(address["phone-number"])
print(address["city"])
print(address["state"])
'''

'''
# To determine how many items a dictionary has, use the len() function:

address = {
"myName": "Rajeev Kumar Singh",
"phone-number": 6299491504,
"address": "btm 2nd stage",
"city": "bangalore",
"state": "karnataka"
}
print(address["myName"])
print(address["phone-number"])
print(address["city"])
print(address["state"])
print("Length of address dictionary is: ",len(address))
'''


'''
# Dictionary Items - Data Types

## The values in dictionary items can be of any data type:



personalDetails = {
"name": "Rajeev Kumar Singh",
"age": 32,
"birthTime": 4.05,
"AMORPM": "AM",
"travelled": ["Patna","Ara","Bangalore","Dubai"],
"City": ("Bangalore","Chennai","Mangalore"),
"Job": {"DevOps", "Engineer"},


}
print(personalDetails)
print("Length of personalDetail Dictionary is: ",len(personalDetails))
print(type(personalDetails))
'''



