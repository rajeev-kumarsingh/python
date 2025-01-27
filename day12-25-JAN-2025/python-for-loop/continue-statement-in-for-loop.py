'''
With the continue statement we can stop the current iteration of the loop, 
and continue with the next:

'''
details = ["Rajeev", "Kumar", "Singh"]
for items in details:
  if items == "Kumar":
    continue
  print(items)


  