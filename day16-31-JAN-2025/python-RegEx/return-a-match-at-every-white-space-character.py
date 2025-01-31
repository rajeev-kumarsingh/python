'''
#Return a match at every white-space character:
r"\s"	Returns a match where the string contains a white space character
'''

import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\s", sentence)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")