'''
+ -One or more occurance
'''
import re

details = 'Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o"'
sample = "hello rajeev"
x = re.findall("he.+o", details)
y = re.findall("he.+o", sample)
print(x)
print(y)
