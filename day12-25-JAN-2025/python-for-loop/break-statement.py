'''
With the break statement we can stop the loop before 
it has looped through all the items
'''
'''
name = ["Rajeev", "Kumar", "Singh"]
# Exit the loop when items is "singh"
for items in name:
  print(items)
  if items == "Singh":
    break

'''
'''
details = ["Rajeev", "Kumar", "Singh", "Devops Engineer"]
print(details)
print(type(details))
for items in details:
  print(items)
  if items == "Singh":
    break
'''
'''
details = ["Rajeev", "Kumar", "Singh", "Devops Engineer"]
print(details)
print(type(details))
for items in details:
  if items == "Singh":
    break
  print(items)
'''
'''
details = {
  "name": "Rajeev Kumar Singh",
  "Age": 32,
  "Profession": "DevOps Engineer"
}
for items in details:
  print(details.items())
  print(details.values())
  if items == "Age":
    break
print("\n")
for items in details:
  if items == "Age":
    break
  print(details.items())
  print(details.values())
'''

details = {
  "name": "Rajeev Kumar Singh",
  "Age": 32,
  "Profession": "DevOps Engineer"
}
for items in details:
  print(items)
  
  if items == "Age":
    break
print("\n")
for items in details:
  if items == "Age":
    break
  print(items)

  