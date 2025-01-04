#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

s = "Rajeev is a nice man"
# check if "good" is not present in the above sentance
print("good" not in s)
print("nice" not in s)
print("man" not in s)
print("country" not in s)
if "nice" not in s:
  print("Yes 'nice' is not present in the above sentance")
elif "is" not in s:
  print("Yes 'is' is not present in the above sentance")
else:
  print("'nice' and 'is' is present in the above sentance")
  