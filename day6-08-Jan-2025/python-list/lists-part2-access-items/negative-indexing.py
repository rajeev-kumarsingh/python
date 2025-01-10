"""
Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
"""
myList = list(("rajeev", "kumar","singh",55, 55.55, True, False))
print(myList)
#from starting 
firstItem = myList[0]
secondItem = myList[1]
thirdItem = myList[2]
fourthItem = myList[3]
fivethItem = myList[4]
lastItem = myList[5]
print(firstItem)
print(secondItem)
print(thirdItem)
print(fourthItem)
print(fivethItem)
print(lastItem)
print("\n")

# from last
item1 = myList[-1]
item2FromLast = myList[-2]
item3FromLast = myList[-3]
item4FromLast = myList[-4]
item5FromLast = myList[-5]
item6FromLast = myList[-6]
print(item1)
print(item2FromLast)
print(item3FromLast)
print(item4FromLast)
print(item5FromLast)
print(item6FromLast)