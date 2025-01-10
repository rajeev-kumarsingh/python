"""
Range of Indexes 
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
"""
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
twoToFive = fruits[2:5] #Note: The search will start at index 2 (included) and end at index 5 (not included).
print(twoToFive)

#By leaving out the start value, the range will start at the first item:
startToFive = fruits[:5] #
print(startToFive) 

#By leaving out the end value, the range will go on to the end of the list:
secondToEnd = fruits[2:]
print(secondToEnd)

#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:
searchFromEnd = fruits[-1:]
print(searchFromEnd)
fruits1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
anotherSearch = fruits1[-1:-4]
print(anotherSearch)