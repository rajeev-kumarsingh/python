"""
There may be times when you want to specify a type on to a variable. T
his can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), 
or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, 
a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
#Integers
x = int(1)
y = int(1.2)
z = int("1")
print(x, type(x))
print(y, type(y))
print(z, type(z))
#Floats
x = float(1)
y = float(2.8)
z = float("2")
a = float("2.8")
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(a, type(a))
#Strings
x = str("s")
y = str(1)
z = str(2.8)
a = str("2.8")
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(a, type(a))