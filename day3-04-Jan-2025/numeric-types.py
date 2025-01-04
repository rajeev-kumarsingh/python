"""
 There are three numeric types in in Python
 1. int - This value is represented by int class. It contains positive or 
 negative whole numbers (without fractions or decimals). In Python, there is no limit to how long an integer value can be.

 2. float - This value is represented by the float class. It is a real number with a floating-point representation. 
 It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be 
 appended to specify scientific notation.

 3. complex - A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j .
   For example - 2+3j
 """
x = 3 # int
y = 3.4 # float
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))

#int
x = 1
y = 12345678909876543
z = -98765
print(type(x))
print(type(y))
print(type(z))

"""
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Float can also be scientific numbers with an "e" to indicate the power of 10.
"""
x = 2.10
y = 0.10
z = -3.20
a = 35e3
b = 12E4
c = -55.7e100
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

"""
Complex numbers are written with a "j" as the imaginary part:

"""
x = 3 + 4j
y = 5j
z = -6j
print(type(x))
print(type(y))
print(type(z))
