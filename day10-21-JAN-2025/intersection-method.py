'''
# 2. Intersection

#- Keep ONLY the duplicates
#- The intersection() method will return a new set, that only contains the items
#  that are present in both sets.

set1 = {1,2,3,4,5,1,2,3,4,5}
set2 = {1,2,3,11,14,10,9,8,}
intersectionResult = set1.intersection(set2)
print(intersectionResult)
print(type(intersectionResult))

'''

'''
# You can use the & operator instead of the intersection() method, 
# and you will get the same result.

  ### Example


set1 = {1,2,3,4,5,1,2,3,4,5}
set2 = {1,2,3,11,14,10,9,8,}
intersectionResult = set1 & set2
print(intersectionResult)
print(type(intersectionResult))

'''

'''
### Note

#### The & operator only allows you to join sets with sets, 
#and not with other data types like you can with the intersection() method.

### Example:
'''
'''
set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]
set1.intersection(set2,tuple1,list1)
print(set1)
print(type(set1))
'''
'''
set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]
intersectionResult = set1 & set2 & tuple1 & list1
print(intersectionResult)
print(type(intersectionResult))

'''

'''
## The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.

set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]
set1.intersection_update(set2,tuple1,list1)
print(set1)
print(type(set1))
'''

## The values True and 1 are considered the same value. The same goes for False and 0.
### Example
set1 = {1,2,3,4,5,6,1,2,8,0,True,False}
tuple1 = (True,0,1,2,3,)
list1 = [1,2,0,3,True,False]
set1.intersection_update(tuple1,list1)
print(set1)
print(type(set1))