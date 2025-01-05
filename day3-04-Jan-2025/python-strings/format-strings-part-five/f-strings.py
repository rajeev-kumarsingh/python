"""
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, 
simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
"""
age = 33
# A placeholder for the age variable 
# placeholder can contain variables, operations, functions, and modifiers
fString = f"My name is Rajeev Kumar Singh and I am {age}"
print(fString)

price = 10000
pricePlaceholder = f"The price is {price} INR"
print(pricePlaceholder)

