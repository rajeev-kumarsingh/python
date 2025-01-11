"""Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""
"""1. Iterating Over a List of Servers
When managing multiple servers, you may want to perform the same task (e.g., deploying code or checking status) across all of them.
"""
#List of running servers
servers = ["server1", "server2", "server3"]

#Using range() and len() to iterate with indices
for i in range(len(servers)):
  print(f"Deploying to {servers[i]}")
  