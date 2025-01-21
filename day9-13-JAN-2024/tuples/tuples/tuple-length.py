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
one_item_tuple = ("Rajeev") #Not a tuple
print(type(one_item_tuple))
one_item_tuple1 = (1) # Not a tuple
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