"""With list comprehension you can do all that with only one line of code"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [i for i in fruits if "a" in i]

print(newList)

newList1 = [i for i in fruits if i != "apple"] # Only accept items that are not "apple":
print(newList1)
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:

