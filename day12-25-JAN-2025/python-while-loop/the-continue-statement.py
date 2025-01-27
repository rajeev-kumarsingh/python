# The continue statement
# With the continue statement we can stop the current iteration, 
# and continue with the next:

i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  print(i)

  