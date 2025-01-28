'''
Key Functions in Sorting
The key parameter in sorted() can use lambda functions to customize sorting
'''

'''

name = ["Rajeev", "Vikash", "Raj", "Vijay", "Shiv"]
sorted_by_length = sorted(name, key=lambda x: len(x)  )
print(sorted_by_length)

'''

'''


# Sort in Descending Order (Longest Names First): Use the reverse=True parameter:

name = ["Rajeev", "Vikash", "Raj", "Vijay", "Shiv"]
sorted_by_length_desc = sorted(name, key=lambda x: len(x), reverse=True  )
print(sorted_by_length_desc)

'''

'''
Sort Alphabetically as a Secondary Key: If two names have the same length,
 you can sort alphabetically by using sorted() with a tuple in the key:

'''
name = ["Rajeev", "Vikash", "Raj", "Vijay", "Shiv"]
sorted_by_length_alpha = sorted(name, key=lambda x: (len(x), x)  )
print(sorted_by_length_alpha)
