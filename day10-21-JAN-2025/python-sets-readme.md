# Python Sets

```
vim  set-example.py
```

```
mysets = {"Rajeev", "Kumar", "Singh"}
print(mysets)
print(type(mysets))
```

Output:

```
python3 set-example.py
```

```
{'Rajeev', 'Kumar', 'Singh'}
<class 'set'>

```

## Set

- Sets are used to store multiple items in a single variable.
- Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
- A set is a collection which is unordered, unchangeable\*, and unindexed.

### <font style="color: red">Note</font>

- Set items are unchangeable, but you can remove items and add new items.
- Sets are unordered, so you cannot be sure in which order the items will appear.

### Set Items

Set items are unordered, unchangeable, and do not allow duplicate values.

### Unordered

- Unordered means that the items in a set do not have a defined order.
- Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

### Example

```
vim  set-example.py
```

```
mysets = {"apple", "mango", "banana", "kiwi", "banana", "apple"}

print(mysets)
```

Output:

```
python3 set-example.py
```

```
{'apple', 'banana', 'kiwi', 'mango'}
<class 'set'>
```

```
python3 set-example.py
```

```
{'apple', 'mango', 'kiwi', 'banana'}
<class 'set'>
```

```
python3 set-example.py
```

```
{'mango', 'apple', 'banana', 'kiwi'}
<class 'set'>
```

```
python3 set-example.py

```

```
{'banana', 'mango', 'apple', 'kiwi'}
<class 'set'>
```

```
python3 set-example.py

```

```
{'mango', 'kiwi', 'apple', 'banana'}
<class 'set'>
```

### Unchangeable

Set items are unchangeable, meaning that we cannot change the items after the set has been created.

<font style="color: red">Note</font> : Once a set is created, you cannot change its items, but you can remove items and add new items.

### Duplicates Not Allowed

Sets cannot have two items with the same value.

Example

```
vim  set-example.py
```

```
mysets = {"apple", "mango", "banana", "kiwi", "banana", "apple"}

print(mysets)
```

Output:

```
python3 set-example.py
```

```
{'apple', 'banana', 'kiwi', 'mango'}
<class 'set'>
```

### <font style="color: red">Note</font> : The values <font style="color: red">True</font> and <font style="color: red">1</font> are considered the same value in sets, and are treated as duplicates:

#### Example: True and 1 is considered the same value:

```
vim  set-example.py
```

```
fruiset = {"apple", "mango", "banana", "kiwi", "banana", "apple", "True", 1 , 2}
print(type(fruiset))
print(fruiset)
```

Output:

```
python3 set-example.py
```

```
{'apple', 'kiwi', 2, 1, 'mango', 'banana', 'True'}
```

### another example

```
vim  set-example.py
```

```
fruiset = {"apple", "mango", "banana", "kiwi", "banana", "apple", True, 1 , 2}
print(type(fruiset))
print(fruiset)
```

Output:

```
python3 set-example.py
```

```
<class 'set'>
{True, 2, 'mango', 'apple', 'banana', 'kiwi'}
```

### <font style="color: red">Note</font> : The values <font style="color: red">False</font> and <font style="color: red">0</font> are considered the same value in sets, and are treated as duplicates:

Examples:

```
vim  set-example.py
```

```
fruiset = {"apple", "mango", "banana", "kiwi", "banana", "apple", True, 1 , 2 , False, 0}
print(type(fruiset))
print(fruiset)
```

Output:

```
python3 set-example.py
```

```
<class 'set'>
{False, 'apple', 2, True, 'mango', 'banana', 'kiwi'}
```

![alt text](image.png)

#

###

# Get the length of the set

```
vim setlength.py
```

```
fruiset = {"apple", "mango", "banana", "kiwi", "banana", "apple", True, 1 , 2 , False, 0}
length=len(fruiset)
print(length)

```

Output:

```
python3 setlength.py
```

```
python3 setlength.py
7
```

![alt text](image-1.png)

#

# Set Items

## Set Items - Data Types

A set can contain different data types:

Set items can be of any data type:

```
vim setitems.py
```

```
set1 = {"Rajeev", "Kumar", "Singh"}
set2 = {1,2,3,1.5}
set3 = {True,True,False,True,False}
set4 = {1.5,5.5,6.5,7.5}
set5 = {1}
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))
print(type(set5))
print(len(set1))
print(len(set2))
print(len(set3))
print(len(set4))
print(len(set5))
```

Output:

```
 python3 setitems.py
```

```
{'Rajeev', 'Singh', 'Kumar'}
{1, 2, 3, 1.5}
{False, True}
{1.5, 5.5, 6.5, 7.5}
{1}
<class 'set'>
<class 'set'>
<class 'set'>
<class 'set'>
<class 'set'>
3
4
2
4
1
```

#

# The set() Constructor

It is also possible to use the set() constructor to make a set.
Example:

```
vim set-constructor.py
```

```
mySet = set(("Rajeev", "Kumar", "Singh"))
print(mySet)
print(len(mySet))
print(type(mySet))
```

Output:

```
python3 set-constructor.py
```

```
{'Kumar', 'Singh', 'Rajeev'}
3
<class 'set'>
```

#

# Python Collections (Arrays)

There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable\*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered\*\* and changeable. No duplicate members.

#

# Access List Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
Example:

```
vim access-setitems.py
```

```
mySet = {"Rajeev", "Kumar", "Singh"}
print(mySet(0))
print(mySet(1))
print(mySet(2))
print(mySet(1,2))
print(mySet( 0,1))
print(len(mySet))
print(type(mySet))

```

Output:

```
python3 access-setitems.py
```

```
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/access-setitems.py", line 3, in <module>
    print(mySet(0))
          ^^^^^^^^
TypeError: 'set' object is not callable
```

![alt text](image-2.png)

#

Example:

```
mySet = {"Rajeev", "Kumar", "Singh"}
print(mySet[1])
print(mySet[2])
print(mySet[3])
print(mySet[1,3])
print(mySet[0,1])
print(len(mySet))
print(type(mySet))
```

Output:

```
python3 access-setitems.py
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/access-setitems.py", line 3, in <module>
    print(mySet[1])
          ~~~~~^^^
TypeError: 'set' object is not subscriptable
```

#

Example
Convert the set to a list or tuple (if the order doesn't matter):

```
mySet = {"Rajeev", "Kumar", "Singh"}
print(list(mySet)[1])
print(list(mySet)[2])
print(list(mySet)[2])
print(list(mySet)[1])
print(list(mySet)[0])
print(len(mySet))
print(type(mySet))

```

Output:

```
╰─ python3 access-setitems.py
Singh
Kumar
Kumar
Singh
Rajeev
3
<class 'set'>

```

#

Iterate over the set to access elements:

```
mySet = {10,20,30,40,50}
for item in mySet:
print(item)
```

Output:

```
python3 access-setitems.py
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/access-setitems.py", line 16
    print(item)
    ^
IndentationError: expected an indented block after 'for' statement on line 3
```

![alt text](image-3.png)

#

```
mySet = {10,20,30,40,50}
for item in mySet:
  print(item)
```

Output:

```
python3 access-setitems.py
50
20
40
10
30
```

![alt text](image-4.png)

#

```
mySet = {10,20,30,40,50}
for item in mySet:
  print(item)

fruits = {"Apple", "Banana", "Kiwi", "Mango"}
for item in fruits:
  print(item)

print("Apple" in fruits)
print("Grapes" not in fruits)
print("Guava" in fruits)
```

Output:

```
python3 access-setitems.py
50
20
40
10
30
Banana
Mango
Apple
Kiwi
True
True
False
```

![alt text](image-5.png)

#

# Change Items

Once a set is created, you cannot change it's items, but you can add new items.

#

# Add Set Items

## Add Items

Once a set is created, you can't change it's item, but you can add new items.

## To add one item to a set use the add() method.

Example:

```
numbers = {10,20,30,40,50}
print(numbers)
newNumber = numbers.add(60)
print(newNumber)
print(numbers)
```

Output:

```
python3 add-set-items.py
{50, 20, 40, 10, 30}
None
{50, 20, 40, 10, 60, 30}
```

![alt text](image-6.png)

```
numbers = {10,20,30,40,50}
print(numbers)
newNumber = numbers.add(60)
print(newNumber)
print(numbers)
seconNumber = numbers.add(70,80,90)
print(numbers)
```

Output:

```
python3 add-set-items.py
{50, 20, 40, 10, 30}
None
{50, 20, 40, 10, 60, 30}
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/add-set-items.py", line 7, in <module>
    seconNumber = numbers.add(70,80,90)
                  ^^^^^^^^^^^^^^^^^^^^^
TypeError: set.add() takes exactly one argument (3 given)
```

#

# Add Sets

To add items from another set into the current set, use the update() method.

```
set1 = {10,20,30,40,50}
set2 = {60,70,10,20,80}
print(set1)
set1.update(set2)
print(set1)
```

Output:

```
python3 add-sets.py
{50, 20, 40, 10, 30}
{70, 40, 10, 80, 50, 20, 60, 30}
```

![alt text](image-7.png)

#

# Add Any Iterable

The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

Example

Add elements of a list to at set:

```
set1 = {10,20,30,40,50}
print(set1)
print(type(set1))
fruits = ["Apple", "Banana", "Kiwi", "Grapes"]
print(fruits)
print(type(fruits))
set1.update(fruits)
print(set1)
```

Output:

```
python3 add-sets.py
{50, 20, 40, 10, 30}
<class 'set'>
['Apple', 'Banana', 'Kiwi', 'Grapes']
<class 'list'>
{10, 20, 'Banana', 30, 'Grapes', 40, 'Kiwi', 50, 'Apple'}
```

![alt text](image-8.png)

#

# Remove Set Item

To remove an item in a set, use the **remove()**, or the **discard()** method.

Example:
ramove "grapes" from fruits list

```
fruits = {"apple","banana", "grapes", "mango"}
print(fruits)
fruits.remove("banana")
print(fruits)
```

Output:

```
python3 remove-set-item.py
{'apple', 'grapes', 'mango', 'banana'}
{'apple', 'grapes', 'mango'}
```

![alt text](image-9.png)

## **Note**: If the item to remove does not exist, remove() will raise an error.

Example

```
fruits = {"apple","banana", "grapes", "mango"}
print(fruits)
fruits.remove("guava")
print(fruits)
```

Output:

```
 python3 remove-set-item.py
{'mango', 'grapes', 'apple', 'banana'}
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/remove-set-item.py", line 4, in <module>
    fruits.remove("guava")
KeyError: 'guava'
```

![alt text](image-10.png)

## Remove "banana" by using the discard() method:

Example:

```
fruits = {"apple","banana", "grapes", "mango"}
print(fruits)
fruits.discard("banana")
print(fruits)
```

Output:

```
python3 remove-set-item.py
{'grapes', 'banana', 'mango', 'apple'}
{'grapes', 'mango', 'apple'}
```

![alt text](image-11.png)

## Note: If the item to remove does not exist, discard() will NOT raise an error.

Example:

```
fruits = {"apple","banana", "grapes", "mango"}
print(fruits)
fruits.discard("Guava")
print(fruits)
```

Output:

```
python3 remove-set-item.py
{'mango', 'banana', 'grapes', 'apple'}
{'mango', 'banana', 'grapes', 'apple'}
```

## You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.
Example:

```
fruits = {"apple","banana", "grapes", "mango"}
print(fruits)
x = fruits.pop("apple")
print(x)

```

Output:

```
{'grapes', 'mango', 'apple', 'banana'}
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/remove-set-item-using-pop-method.py", line 5, in <module>
    fruits.pop("apple")
TypeError: set.pop() takes no arguments (1 given)
```

![alt text](image-12.png)

```
fruits = {"apple","banana", "grapes", "mango"}
print(fruits)
x = fruits.pop()
print(x)
```

Output:

```
python3 remove-set-item-using-pop-method.py
{'mango', 'grapes', 'apple', 'banana'}
mango
```

![alt text](image-13.png)

## Note

#### Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#

# clear() method

#### The clear() method empties the set:

Example:

```
fruits = {"apple", "banana", "mango"}
print(fruits)
print(type(fruits))
clearItems = fruits.clear()
print(clearItems)
print(type(clearItems))
```

Output:

```
python3 clear-method-in-set.py
{'banana', 'mango', 'apple'}
<class 'set'>
None
<class 'NoneType'>
```

![alt text](image-14.png)

#

# The del keyword will delete the set completely:

Eampled:

```
fruits = {"apple", "banana", "mango"}
print(fruits)
print(type(fruits))
del fruits
print(fruits)
print(type(fruits))
```

Output:

```
python3 del-keyword-in-set.py
{'mango', 'apple', 'banana'}
<class 'set'>
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/del-keyword-in-set.py", line 9, in <module>
    print(fruits)
          ^^^^^^
NameError: name 'fruits' is not defined
```

![alt text](image-15.png)

#

# Join Sets

## There are several ways to join two or more sets in Python

- The **union()** and **update()** methods joins all items from both sets.
- The **intersection()** method keeps ONLY the duplicates.
- The **difference()** method keeps the items from the first set that are not in the other set(s).
- The **symmetric_difference()** method keeps all items EXCEPT the duplicates.

##

1. **union()** and **update()** method to join sets

   - example of union(): join two sets into a new set

   ```
   fruits = {"apple", "banana", "mango"}
   players = {"sachin", "sehwag", "dhoni"}
   print(fruits)
   print(players)

   mixedSet = fruits.union(players)
   print(mixedSet)

   ```

   Output:

   ```
    python3 union-and-update-method.py
    {'banana', 'apple', 'mango'}
    {'sehwag', 'sachin', 'dhoni'}
    {'banana', 'sehwag', 'apple', 'dhoni', 'sachin', 'mango'}
   ```

   ### You can use the | operator instead of the union() method, and you will get the same result.

   ```
   fruits = {"apple", "banana", "mango"}
   players = {"sachin", "sehwag", "dhoni"}
   print(fruits)
   print(players)

   mixedSet = fruits | players
   print(mixedSet)

   ```

   Output:

   ```
    python3 union-and-update-method.py
    {'mango', 'banana', 'apple'}
    {'sachin', 'sehwag', 'dhoni'}
    {'mango', 'banana', 'sachin', 'dhoni', 'sehwag', 'apple'}
   ```

   ![alt text](image-16.png)

   #

   ### Join Multiple Sets

   All the joining methods and operators can be used to join multiple sets.

   When using a method, just add more sets in the parentheses, separated by commas:

   Example:
   Join multiple sets with the **union()** method

   ```
   set1 = {1,2,3,4,5}
   set2 = {11,22,33,44,55}
   set3 = {111,222,333,444,555}
   set4 = {1111,2222,3333,4444,5555}
   mixed = set1.union(set2,set3,set4)
   print(mixed)
   print(type(mixed))
   ```

   Output:

   ```
   python3 union-and-update-method.py
   {1, 2, 3, 4, 5, 3333, 11, 333, 22, 1111, 4444, 222, 33, 555, 44, 2222, 111, 5555, 55, 444}
   <class 'set'>
   ```

   ![alt text](image-17.png)

   #

   # When using the | operator, separate the sets with more | operators:

   Example:

   ```
   set1 = {1,2,3,4,5}
   set2 = {11,22,33,44,55}
   set3 = {111,222,333,444,555}
   set4 = {1111,2222,3333,4444,5555}
   mixed = set1 | set2 | set3 | set4
   print(mixed)
   print(type(mixed))
   ```

   Output:

   ```
   python3 union-and-update-method.py
   {1, 2, 3, 4, 5, 3333, 11, 333, 22, 1111, 4444, 222, 33, 555, 44, 2222, 111, 5555, 55, 444}
   <class 'set'>
   ```

   ![alt text](image-18.png)

   #

   # Join a Set and a Tuple

   Example:

   ```
   set1 = {1,2,3,4,5}
   set2 = {11,22,33,44,55}
   set3 = {111,222,333,444,555}
   set4 = {1111,2222,3333,4444,5555}
   tuple1 = (111111,222222,333333,4444444,555555)
   tupleandset = set1.union(set2,set3,set4,tuple1)
   print(tupleandset)
   print(type(tupleandset))
   ```

   Output:

   ```
   python3 union-and-update-method.py
   {1, 2, 3, 4, 5, 3333, 111111, 11, 333, 222222, 333333, 22, 1111, 4444, 4444444, 222, 33, 555555, 555, 44, 2222, 111, 5555, 55, 444}
   <class 'set'>
   ```

   ![alt text](image-20.png)

   ### Note

   The | operator only allows you to join sets with sets, and not with other data types like you can with the union() method.

   #

   - example of **update()**: join two sets into a new set

     ### Update

     - The update() method inserts all items from one set into another.

     - The update() changes the original set, and does not return a new set.

     Example:

     ```
     set1 = {1,2,3,4,5}
     set2 = {11,22,33,44,55}
     set3 = {111,222,333,444,555}
     set4 = {1111,2222,3333,4444,5555}
     tuple1 = (111111,222222,333333,4444444,555555)
     set1.update(set2,set3,set4,tuple1)
     print(set1)
     print(type(set1))
     ```

     Output:

     ```
     python3 union-and-update-method.py
     {1, 2, 3, 4, 5, 3333, 111111, 11, 333, 222222, 333333, 22, 1111, 4444, 4444444, 222, 33, 555555, 555, 44, 2222, 111, 5555, 55, 444}
     <class 'set'>
     ```

     ![alt text](image-21.png)

     #

     ## Note

     Both **union()** and **update()** will exclude any duplicate items.
     Example:

     ```
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
     ```

     Output:

     ```
     python3 union-and-update-method.py
     {1, 2, 3, 4, 5, 3333, 111111, 55555, 11, 333, 222222, 22222, 333333, 22, 1111, 4444, 4444444, 222, 44444, 33, 555555, 11111, 555, 44, 2222, 111, 5555, 33333, 55, 444}
     <class 'set'>
     {1, 2, 3, 4, 5, 3333, 111111, 55555, 11, 333, 222222, 22222, 333333, 22, 1111, 4444, 4444444, 222, 44444, 33, 555555, 11111, 555, 44, 2222, 111, 5555, 33333, 55, 444}
     <class 'set'>
     ```

     ![alt text](image-22.png)

# 2. Intersection

- Keep ONLY the duplicates
- The intersection() method will return a new set, that only contains the items that are present in both sets.

### Example:

     ```
     set1 = {1,2,3,4,5,1,2,3,4,5}
     set2 = {1,2,3,11,14,10,9,8,}
     intersectionResult = set1.intersection(set2)
     print(intersectionResult)
     print(type(intersectionResult))

     ```

Output:

     ```
     python3 intersection-method.py
     {1, 2, 3}
     <class 'set'>
     ```

![alt text](image-23.png)

### You can use the & operator instead of the intersection() method, and you will get the same result.

### Example

```
set1 = {1,2,3,4,5,1,2,3,4,5}
set2 = {1,2,3,11,14,10,9,8,}
intersectionResult = set1 & set2
print(intersectionResult)
print(type(intersectionResult))
```

Output:

```
python3 intersection-method.py
{1, 2, 3}
<class 'set'>
```

![alt text](image-24.png)

### Note

#### The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

### Example:

```
set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]
set1.intersection(set2,tuple1,list1)
print(set1)
print(type(set1))

'''
set1 = {1,2,3,4,5,1,2,3,4,5}
set2 = {1,2,3,11,14,10,9,8,}
tuple1 = (232,123,324,23232,23233,222222)
list1 = [2222,222222,222222,222222,222222,22222222,2222,22222]
intersectionResult = set1 & set2 & tuple1 & list1
print(intersectionResult)
print(type(intersectionResult))

'''
```

Output:

```
python3 intersection-method.py
{1, 2, 3, 4, 5, 6, 8}
<class 'set'>

```

![alt text](image-25.png)

### The & operator only allows you to join sets with sets, and not with other data types

```
'''
set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]
set1.intersection(set2,tuple1,list1)
print(set1)
print(type(set1))
'''

set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]


```

Output:

```
python3 intersection-method.py
Traceback (most recent call last):
  File "/Users/rajeevsingh/Documents/learning-python/day10-21-JAN-2025/intersection-method.py", line 53, in <module>
    intersectionResult = set1 & set2 & tuple1 & list1
                         ~~~~~~~~~~~~^~~~~~~~
TypeError: unsupported operand type(s) for &: 'set' and 'tuple'
```

![alt text](image-26.png)

## The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

```
set1 = {1,2,3,4,5,6,1,2,8}
set2 = {1,2,3,11,14,10,9,6,8,232}
tuple1 = (232,11,324,23232,6,23233,8)
list1 = [232,11,3232,4444,6,8]
set1.intersection_update(set2,tuple1,list1)
print(set1)
print(type(set1))
```

Output:

```
python3 intersection-method.py
{8, 6}
<class 'set'>
```

![alt text](image-27.png)

## The values True and 1 are considered the same value. The same goes for False and 0.

### Example

```
set1 = {1,2,3,4,5,6,1,2,8,0,True,False}
tuple1 = (True,0,1,2,3,)
list1 = [1,2,0,3,True,False]
set1.intersection_update(tuple1,list1)
print(set1)
print(type(set1))
```

Output:

```
python3 intersection-method.py
{0, 1, 2, 3}
<class 'set'>
```

![alt text](image-28.png)
