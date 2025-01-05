"""
Split String: The split() method returns a list where the text between the specified separator becomes the list items.
The split() method splits the string into substrings if it finds instances of the separator:

"""
s = 'Rajeev, Kumar, Singh'
t = 'rajeev. singh'
print(s.split(","))
print(s.split("."))
print(t.split(","))
print(t.split("."))

print(s.split(" "))
print(t.split(" "))

print(s.split(""))
print(t.split(""))


