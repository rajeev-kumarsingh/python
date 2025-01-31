'''
#Check if the string contains any digits (numbers from 0-9):

\d -Returns a match where the string contains digits (numbers from 0-9)	
'''

import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\d", sentence)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")