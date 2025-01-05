"""
Remove whitespace: whitespace is the space before and/or after the actual text, and very often you want to remove the space

The strip() method remove any whitespace from the beginning or the end.
"""
s = " 'In this string, one whitespace is at the beginning and and one at the end' "
print("String:", s)
# Remove whitespace
print("use strip() method to remove whitespace")
print("Remove whitespace: s.strip()", s.strip())
