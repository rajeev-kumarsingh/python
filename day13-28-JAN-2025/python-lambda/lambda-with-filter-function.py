'''
Used with filter()
The filter() function filters elements based on a condition
'''
nums = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # Output: [2, 4, 6]
