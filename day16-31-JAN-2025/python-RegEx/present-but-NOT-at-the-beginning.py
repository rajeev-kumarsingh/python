'''
#Check if "ain" is present, but NOT at the beginning of a word:
\B -Returns a match where the specified characters are present,
 but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being 
treated as a "raw string")
'''

import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\Bain", sentence)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")