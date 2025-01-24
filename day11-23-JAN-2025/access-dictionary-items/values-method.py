# The values() method will return a list of all the values in the dictionary.

course = {
 "name": "DevOps",
 "UsedIn": "IT Operations",
 "Duration": 10.5,
 "Type": "Months"

}
print("course dictionary is:", course)
print("length of course dictionary is: ", len(course))
print("name of the course is: ", course["name"])
print("where we can use DevOps: ", course.get("UsedIn"))
print("Values of course dictionary before change is:  ", course.values())
print("course dictionary key before adding a new item is: ", course.keys())
course["Duration"] = 8
print("course dictionary values after change is: ", course.values())
# Add a new item to the original dictionary, and see that the values list gets updated as well:
course["Enroll"] = "ASAP"
print("Updated course dictionary values after adding a new item is: ", course.values())
print("course dictionary keys after adding a new item is: ", course.keys())
