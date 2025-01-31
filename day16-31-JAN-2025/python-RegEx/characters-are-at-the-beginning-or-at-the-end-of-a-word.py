'''
\b -Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
Ex - r\bain
'''
import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bSpain", sentence)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")