#To check if a certain phrase or character is present in a string, we can use the keyword in.
s = 'Rajeev works for IBM as DevOps engineer'
# check if DevOps is present in the following sentance or not
print("DevOps" in s)
print("devops" in s)
print("Devops" in s)
print("IBM" in s)
print("for" in s)
print("Engineer" in s)
if "Works" in s:
  print("Yes 'works' is present in the above sentance")
elif "For" in s:
  print("No 'For is not present in the above sentance'")
else:
  print("No 'Works' and 'For' is not present in the above sentance")
  

