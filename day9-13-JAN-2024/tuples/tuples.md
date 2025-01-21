# Python Tuples

mytuple = ("apple", "banana", "cherry")
Tuple
Tuples are used to store multiple items in a single variable.

- Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

- A tuple is a collection which is ordered and unchangeable.

- Tuples are written with round brackets.

![alt text](image.png)

stringTuple = ("one", "two", "three", "four", "five") #Tuples are written in round brackates
intTuple = (1,2,3,4,5)
mixedTuple = (1,2,3,4,5,"one", "two", "three", "four", "five")
print(stringTuple)
print(intTuple)
print(mixedTuple)
Output
python3 tuples.py
('one', 'two', 'three', 'four', 'five')
(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5, 'one', 'two', 'three', 'four', 'five')
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Allow Duplicates
Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
Tuple Length
To determine how many items a tuple has, use the len() function:
"""Tuple length
To determine how many items a tuple has, use the len() function:

"""
myTuple = (1,2,3,4,5,"one","two",1.2,True,False)
length_myTuple = len(myTuple)
print(myTuple)
print(length_myTuple)

"""OutPut:
python3 tuple-length.py
(1, 2, 3, 4, 5, 'one', 'two', 1.2, True, False)
10"""

# Create tuple with one item

one_item_tuple = ("Rajeev")
print(type(one_item_tuple))
one_item_tuple1 = (1)
print(one_item_tuple1)
print(type(one_item_tuple1))
"""Output:
<class 'str'>
1
<class 'int'>"""
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
one_item_tuple2 = ("Rajeev",)
one_item_tuple3 = (2,)
print(type(one_item_tuple2))
print(type(one_item_tuple3))
"""Output:
<class 'tuple'>
<class 'tuple'>"""

Tuple Constructor- tuple()
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
Using the tuple() method to make a tuple:
"""The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple."""
#Using the tuple() method to make a tuple:
myTuple = tuple(("Rajeev","Kumar","Singh", 5,5.5, True))
print(myTuple)
print(type(myTuple))
"""Output:
python3 tuple-constructor.py
('Rajeev', 'Kumar', 'Singh', 5, 5.5, True)
<class 'tuple'>"""

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable\*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered\*\* and changeable. No duplicate members.

\*Set items are unchangeable, but you can remove and/or add items whenever you like.

\*\*As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
