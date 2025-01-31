'''
You can control the number of replacements by specifying the count parameter:

Replace the first 2 occurrences:
'''

import re

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt, 2)
print(x)