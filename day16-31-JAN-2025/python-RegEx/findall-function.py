'''
# findall()
# Returns a list containing all matches.
# Metacharacter- []
'''


'''
import re

txt = "I am learning RegEx or Regular Expression, is a sequence of characters that forms a search pattern. "

# Find all lower case characters alphabetically between "a" and "m"
x = re.findall("[a-m]", txt)
print(x)

'''



'''
import re
txt = "That will be 59 rupees"

#Find all digit characters:

x = re.findall("\d", txt)
# Find small letters between a to f
y = re.findall("[a-f]", txt)
print(x)
print(y)
'''




'''
# Metacharacter
# .	- Any character (except newline character)

import re 
txt =  "hello rajeev"
txt1 = "Great, you are learning RegEx or Regular Expression"
# Search for a sequence that start with "G", followed by three (any) characters, and an "t".
y = re.findall("G....", txt1)
# Search for a sequence that start with "he", followed by two (any) characters, and an "o".
x = re.findall("he..o", txt)
print(x)
print(y)
'''


import re
txt = "hello Rajeev"

# #Check if the string starts with 'hello':
x = re.findall("^hello", txt)
print(x)