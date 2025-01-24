# Change values  and add items

course = {
 "name": "DevOps",
 "UsedIn": "IT Operations",
 "Duration": 10.5,
 "Type": "Months"

}
print("Before change: ", course)
print("Items before change: ", course.items())
print("Values before change: ", course.values())
# Change Values 
course["Duration"] = 7
course["UsedIn"] = "Operations Works in IT company"
# Add items
course["Platform"] = "Online"
print("After change: ", course)
print("Items after change: ", course.items())
print("Values after change: ", course.values())
# update the  "Duration" of the course by using the update() method
course.update({"Duration": "9"})
course.update({"fullName": "Rajeev Kumar Singh"})
print(course.values())
print(course.items())

