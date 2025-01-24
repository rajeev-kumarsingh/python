
'''
# The items() method will return each item in a dictionary, as tuples in a list.

course = {
 "name": "DevOps",
 "UsedIn": "IT Operations",
 "Duration": 10.5,
 "Type": "Months"

}
print(course)
print("\n")
print(course.keys())
print("\n")
print(course.values())
print("\n")
print("course dictionary items before change",course.items())
print("\n")
print(len(course))
#The returned list is a view of the items of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the items list.
course["Duration"] = 8
course["enroll"] = "ASAP"
print("course dictionary items after changes: ", course.items())
'''

course = {
 "name": "DevOps",
 "UsedIn": "IT Operations",
 "Duration": 10.5,
 "Type": "Months"

}
if "name" in course:
  print("Yes, 'name'  is one of the key in the course dictionary! ")
  