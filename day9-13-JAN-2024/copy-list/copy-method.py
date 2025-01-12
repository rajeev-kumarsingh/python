"""Copy a list using built in method copy()"""
fruits = ["Mango", "Banana", "Apple",  "Orange", "Grapes","Pinaple"]
newList = fruits
print(newList)
"""Output till now 
python3 copy-method.py 
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange']"""
# Lets change the fruits list and see the effect on newList 
print(newList)
"""You cannot copy a list simply by typing list2 = list1, because: 
list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2."""
"""Output:
 python3 copy-method.py
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange', 'Grapes']
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange', 'Grapes']"""

#use copy()method
newList1 = fruits.copy()
print(newList1)

# Now let's change the list value of fruits 
print(newList1)
"""Output:
python3 copy-method.py
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Kiwi', 'Orange', 'Grapes', 'Pinaple']"""
# Let's delete one item from fruits list , removed kiwi from fruits list 
#print newList and newList1
print(newList)
print(newList1)
"""OutPut:
 python3 copy-method.py
['Mango', 'Banana', 'Apple', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Orange', 'Grapes', 'Pinaple']
['Mango', 'Banana', 'Apple', 'Orange', 'Grapes', 'Pinaple']"""
