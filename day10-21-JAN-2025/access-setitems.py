###List items are indexed ans you can access them by referring to the index number

#Convert the set to a list or tuple (if the order doesn't matter):
#mySet = {"Rajeev", "Kumar", "Singh"}
#print(list(mySet)[1])
#print(list(mySet)[2])
#print(list(mySet)[2])
#print(list(mySet)[1])
#print(list(mySet)[0])
#print(len(mySet))
#print(type(mySet))


mySet = {10,20,30,40,50}
for item in mySet:
  print(item)

fruits = {"Apple", "Banana", "Kiwi", "Mango"}
for item in fruits:
  print(item)

print("Apple" in fruits)
print("Grapes" not in fruits)
print("Guava" in fruits)
