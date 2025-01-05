We can not combine string and integer like this

age = 33

s = 'My name is Rajeev and my age is ' + age

We will get error
Traceback (most recent call last):
File "/Users/rajeevsingh/Documents/learning-python/day3-04-Jan-2025/python-strings/format-strings-part-five/format-string.py", line 5, in <module>
s = 'My name is Rajeev and my age is ' + age

```^~~~~
TypeError: can only concatenate str (not "int") to str


But we can combine strings and numbers by using f-strings or the format() method!

F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

```

age = 33

s = f'My name is Rajeev and my age is {age}'
print(s)

Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
Example
Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
Example
Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

A placeholder can contain Python code, like math operations:
Example
Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 \* 59} dollars"
print(txt)
