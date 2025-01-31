
import re
txt = "The rain in Spain"
#Split the string only at the first occurrence:
x = re.split(r"\s", txt, 1)
#Split the string only at the first and second occurrence:

y = re.split(r"\s", txt, 2)
print(x)
print(y)