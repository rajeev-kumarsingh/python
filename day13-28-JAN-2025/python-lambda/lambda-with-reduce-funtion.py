'''
Used with reduce()
The reduce() function (from functools) applies a function cumulatively to the items in a sequence
'''
from functools import reduce
nums = [1,2]
product = reduce(lambda x, y: x*y, nums)
print(product)
print("\n")
nums = [1,2,3]
product = reduce(lambda x, y: x*y, nums)
print(product)
print("\n")
nums = [1,2,3,4]
product = reduce(lambda x, y: x*y, nums)
print(product)
print("\n")
nums = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, nums)
print(product)
print("\n")
nums = [1,2,3,4,5,6]
product = reduce(lambda x, y: x*y, nums)
print(product)
