import re

# Search the string to see if it starts with "The" and ends with "Spain":
txt =  "The rain in Spain"
x = re.search("^The.*Spain$", txt)

'''
^The ensures that the string starts with "The".
.* allows any number of characters (including none) between "The" and "Spain".
Spain$ ensures that the string ends with "Spain".
'''