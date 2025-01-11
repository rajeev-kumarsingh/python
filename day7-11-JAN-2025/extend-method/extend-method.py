"""
Here’s a practical example of using the extend() method in a DevOps scenario. 
The extend() method is used to add multiple items (from another iterable, 
like a list) to the end of an existing list.
"""
"""
using extend() to Update server inventory
Suppose you have a list of server currently in production, and you need to add new server from currently provisioned
batch to the list. 
"""
#Current list of production server 
prod_server = ["prod-server1.example.com", "prod-server2.example.com"]
print("Current server list: ", prod_server)

#New server to be added 
new_server = ["prod.server3.example.com", "prod-server4.example.com"]

# Extend the production server list with the new server 
prod_server.extend(new_server)
#Print the extended server list 
print("Extended Server List: ", prod_server)
