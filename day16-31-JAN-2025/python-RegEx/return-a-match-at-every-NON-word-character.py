'''
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
\W	Returns a match where the string DOES NOT contain any word characters
'''

import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\W", sentence)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")