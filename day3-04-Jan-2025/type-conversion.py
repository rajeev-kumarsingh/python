"""
you can convert one type to another with int(), float() and complex() method
"""
x = 55 #int
y = 55.55 #float
z = 55j # complex
print(type(x))
print(type(y))
print(type(z))
# convert from int to float
a = float(x)
print(type(a))
# Convert from float to int
b = int(y)
print(type(b))
#Convert from int to complex
d = complex(x)
print(type(d))
# Convert from complex to int
c = int(z)
print(type(c))
