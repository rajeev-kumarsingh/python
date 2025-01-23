# Union() and Update() method

'''
# The union() method returns a new set with all items from both sets.
fruits = {"apple", "banana", "mango"}
players = {"sachin", "sehwag", "dhoni"}
print(fruits)
print(players)

mixedSet = fruits.union(players)
print(mixedSet)

'''

'''
# Use | operator
fruits = {"apple", "banana", "mango"}
players = {"sachin", "sehwag", "dhoni"}
print(fruits)
print(players)

#mixedSet = fruits | players
#print(mixedSet)
'''

'''
 #Join multiple sets with union() method
set1 = {1,2,3,4,5}
set2 = {11,22,33,44,55}
set3 = {111,222,333,444,555}
set4 = {1111,2222,3333,4444,5555}
mixed = set1.union(set2,set3,set4)
print(mixed)
print(type(mixed))
'''

'''
When using the | operator, separate the sets with more | operators:
set1 = {1,2,3,4,5}
set2 = {11,22,33,44,55}
set3 = {111,222,333,444,555}
set4 = {1111,2222,3333,4444,5555}
mixed = set1.union(set2,set3,set4)
print(mixed)
#print(type(mixed))
'''
'''
 Join a Set and a Tuple
set1 = {1,2,3,4,5}
set2 = {11,22,33,44,55}
set3 = {111,222,333,444,555}
set4 = {1111,2222,3333,4444,5555}
tuple1 = (111111,222222,333333,4444444,555555)
tupleandset = set1.union(set2,set3,set4,tuple1)
print(tupleandset)
print(type(tupleandset))

# Join set with update() method
set1 = {1,2,3,4,5}
set2 = {11,22,33,44,55}
set3 = {111,222,333,444,555}
set4 = {1111,2222,3333,4444,5555}
tuple1 = (111111,222222,333333,4444444,555555)
set1.update(set2,set3,set4,tuple1)
print(set1)
print(type(set1))
'''

'''
#Both union() and update() exclude duplicates

set1 = {1,2,3,4,5,1,2,3,4,5}
set2 = {11,22,33,44,55,11,22,33,44,55}
set3 = {111,222,333,444,555,111,222,333,444,555}
set4 = {1111,2222,3333,4444,5555,1111,2222,3333,4444,5555}
tuple1 = (111111,222222,333333,4444444,555555,11111,22222,33333,44444,55555)
set1.update(set2,set3,set4,tuple1)
mixed = set1.union(set2,set3,set4,tuple1)
print(set1)
print(type(set1))
print(mixed)
print(type(mixed))

'''

