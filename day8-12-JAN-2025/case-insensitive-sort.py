"""Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

"""
#Case sensitive sorting can give an unexpected result:
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort()
print(fruits)
"""Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:"""
#Perform a case-insensitive sort of the list:
fruits.sort(key = str.lower)
print(fruits)

"""Output:
python3 case-insensitive-sort.py
['Kiwi', 'Orange', 'banana', 'cherry']
['banana', 'cherry', 'Kiwi', 'Orange']"""