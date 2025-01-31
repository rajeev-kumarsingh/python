'''
Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
{} -Exactly specified number of occurance
'''
import re

greet = "hello Rajeev"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
search1 = 'Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o"- hello learner, love me'
x = re.findall("he.{2}o", greet)
y = re.findall("he.{2}o", search1)
z = re.findall("lo.{4}e", search1)
print(x)
print(y)
print(z)

