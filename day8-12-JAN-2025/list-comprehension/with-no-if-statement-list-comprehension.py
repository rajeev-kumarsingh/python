# With no if statement 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [i for i in fruits]
print(newList)

#iterable
#The iterable can be any iterable object, like a list, tuple, set,etc
newList1 = [i for i in range(10)]
print(newList1)
newList2 = [i for i in range(10)]
print(newList2)

#Some Example, but with a condition
newList3 = [i for i in range(10) if i <= 5] #Accept only number lower than 5 or equal to 5
print(newList3)

newList4 = [i.upper() for i in fruits]
print(newList4)

#You can set the outcome to whatever you like:
newList5 = ["hello" for i in fruits]
print(newList5)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":
newList6 = [i if i != "banana" else "orange" for i in fruits] # Return "orange" instead of "banana":
print(newList6)
"""The expression in the example above says:
"Return the item if it is not banana, if it is banana return orange"."""
