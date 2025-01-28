# Example of removing Array elements

# Create an array
items = ["item1", "item2", "item3", "item4"]
print("Before addition: ", items)
# add new item 
items.append("item5")
print("After addition: ", items)
print("\n")
# Remove an array element
# You can use the pop() method to remove an element from the array.
items.pop(0)
print("Removed zeroth index element with pop() method: ",items)

# You can also use the remove() method to remove an element from the array.
items1 = ["item1", "item2", "item3", "item4"]
print("Before removal of an array elements: ", items1)
print("\n")
# remove an array elements with remove()
items.remove("item3")
print("After removal an array elements with remove(): ", items)
# check the type after an array element removal
print(type(items1))

# The list's remove() method only removes the first occurrence of the specified value



