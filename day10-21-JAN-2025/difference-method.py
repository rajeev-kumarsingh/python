"""
Difference:
The difference() method will return a new set that will contain only the items from the first set
 that are not present in the other set.

"""
'''
# Example
set1 = {"Rajeev", "Kumar", "Singh","DevOps"}
list1 = ["DevOps"]
tuple1 = ("Singh", "Engineer")
set1.difference(list1,tuple1)
set1Dif = set1.difference(list1)
set1Dif2 = set1.difference(tuple1)
print(set1)
print(type(set1))
print(type(list1))
print(type(tuple1))
print(set1Dif)
print(set1Dif2)
'''
'''
## You can use the **-** operator instead of the difference() method, 
# and you will get the same result.

## Example
'''

'''
set1 = {"Rajeev", "Kumar", "Singh","DevOps"}
set2 = {"Kumar", "Singh"}
# use the - operator instead of difference() method 
#The - operator only allows you to join sets with sets, 
# and not with other data types like you can with the difference() method.
set1MinusOperator = set1-set2
list1 = ["DevOps"]
tuple1 = ("Singh", "Engineer")
set1.difference(list1,tuple1)
set1Dif = set1.difference(list1)
set1Dif2 = set1.difference(tuple1)
print(set1)
print(type(set1))
print(type(list1))
print(type(tuple1))
print(set1Dif)
print(set1Dif2)
'''
'''
# difference_update()

## The difference_update() method will also keep the items from the first set
#  that are not in the other set, but it will change the original set 
# instead of returning a new set.

## Example:

set1 = {"apple", "mango", "kiwi", "banana"}
set2 = {"kiwi", "grapes", "banana"}
setDifferenceUpdate = set1.difference_update(set2)
set1.difference_update(set2)
print(setDifferenceUpdate)
print( "Type of setDifferenceUpdate is ",type(setDifferenceUpdate))
print(set1)
print(type(set1))


'''



'''

# Symmetric Differences
## The symmetric_difference() method will keep only the elements that are NOT present in both sets.

## Example:

set1 = {"apple", "mango", "kiwi", "banana"}
set2 = {"kiwi", "grapes", "banana"}
setDifferenceUpdate = set1.symmetric_difference(set2)
set1.symmetric_difference(set2)
print(setDifferenceUpdate)
print( "Type of setDifferenceUpdate is ",type(setDifferenceUpdate))
print(set1)
print(type(set1))

'''

'''
## You can use the ^ operator 
# instead of the symmetric_difference() method, and you will get the same result.


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

'''




## Note

#### The ^ operator only allows you to join sets with sets, 
# and not with other data types like you can with the symmetric_difference() method.

#Example:
'''
set1 = {"apple", "banana", "cherry"}
list1 = ["google", "microsoft", "apple"]

#set1.difference_update(list1)
set3 = set1 ^ list1
#print(set1)
print(set3)
'''

'''
# symmetric_difference_update()

## The symmetric_difference_update() method will also keep all but 
# the duplicates, but it will change the original set instead of returning a new set.

### Example:

#### Use the symmetric_difference_update() method to keep the items 
# that are not present in both sets:
'''


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
print(type(set1))
