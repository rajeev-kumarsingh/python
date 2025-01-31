
'''
The split() Function
The split() function returns a list where the string has been split at each match:
'''
import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)