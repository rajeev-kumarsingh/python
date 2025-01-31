'''
| -Either or 

Check if the string contains either "falls" or "stays
'''
import re

sentance = "The rain in India falls mainly in the plain and stays for long! "
x = re.findall("falls|stays", sentance)
print(x)
if x:
  print("Yes, There is both match")
else:
  print("No Match")
