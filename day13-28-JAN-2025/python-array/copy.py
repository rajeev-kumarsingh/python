# copy() method

items = ["item1", "item2", "item3", "item4"]
print("items array elements: ", items)
newItem = items.copy()
print("newItem array elements",newItem)
# Let add one more element in items element to check newItem array is also gettin updated or not
items.append("item5")
print("After addition of new elements in items array: ",items)
print("newItem array element: ", newItem)


