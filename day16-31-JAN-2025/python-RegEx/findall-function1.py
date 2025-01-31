
'''


import re
txt = "hello Rajeev"

# #Check if the string starts with 'hello':
x = re.findall("^hello", txt)
print(x)
'''

import re
txt = "hello Rajeev"

# #Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No Match")

