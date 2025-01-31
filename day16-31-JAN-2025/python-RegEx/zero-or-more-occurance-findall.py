'''
* -Zero or more occurance
'''
import re
sample = "hello rajeev"
details = "Search for a sequence that starts with 'he', followed by 0 or more  (any) characters, and an 'o', hello rajeev"
x = re.findall("he.*o", details)
y = re.findall("he.*o", sample)
print(x)
print(y)
