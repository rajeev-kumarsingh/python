"""
A placeholder can contain Python code, like math operations:

Perform a math operation (20 * 59) in the placeholder, and return the result:

"""
fStringPlaceholderWithOperation = f'The price is {5000 * 2} INR'
print(fStringPlaceholderWithOperation) # Returns The price is 10000
fstringPlaceholderWithOpersationAndModifier = f"The price is {5000 * 2:.2f} INR"
print(fstringPlaceholderWithOpersationAndModifier) # Returns The price is 10000.00
