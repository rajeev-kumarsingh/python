'''
$ - Ends with  findall 
'''
'''

import re

details = "check if the string ends with 'planet'"
x = re.findall("planet$", details)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No Match")
'''

import re

details = "check if the string ends with 'planet'"
x = re.findall("'planet'$", details)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No Match")