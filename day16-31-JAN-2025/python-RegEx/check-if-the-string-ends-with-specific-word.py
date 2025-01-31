'''
#Check if the string ends with "Spain":

\Z	Returns a match if the specified characters are at the end of the string
'''


import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"Spain\Z", sentence)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")