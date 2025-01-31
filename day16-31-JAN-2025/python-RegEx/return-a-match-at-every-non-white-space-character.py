'''
#Return a match at every NON white-space character:

\S -Returns a match where the string DOES NOT contain a white space character	
'''
import re

sentence = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\S", sentence)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")