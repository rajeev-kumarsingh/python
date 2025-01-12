"""Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements."""
#Reverse the order of the list items:
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.reverse()
print(fruits)

"""python3 reverse-oreder.py             
['cherry', 'Kiwi', 'Orange', 'banana']"""

name = ["z", "a", "ab", "f", "g","ghg", "b","e","d"]
name.reverse()
print(name)

"""Output:
python3 reverse-oreder.py
['cherry', 'Kiwi', 'Orange', 'banana']
['d', 'e', 'b', 'ghg', 'g', 'f', 'ab', 'a', 'z']"""