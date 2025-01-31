'''
specified characters are at the beginning of the string

\A -Return a match if the specifies character is at the beginning of the string.
'''
import re

sentence = "The rain in India"
# check if the string start with 'the'
x = re.findall(r"\AThe", sentence)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")