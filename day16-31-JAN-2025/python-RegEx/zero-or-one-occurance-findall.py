
'''
? -Zero or one occurance
'''
import re

details = 'Search for a sequence that starts with "he", followed by o or one  (any) characters, and an "o"'
sample = "hello rajeev"
x = re.findall("he.?o", details)
y = re.findall("he.?o", sample)
print(x)
print(y)

details = 'rest rajeev'
#"re", followed by 0 or one  (any) characters, and an "q"'
sample = "req rajeev"
x = re.findall("re.?t", details)
y = re.findall("re.?q", sample)
print(x)
print(y)
