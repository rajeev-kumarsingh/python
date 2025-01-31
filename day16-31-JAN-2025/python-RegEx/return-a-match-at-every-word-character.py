'''
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

\w	Returns a match where the string contains any word characters
 (characters from a to Z, digits from 0-9, and the underscore _ character)
'''

import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\w", sentence)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")