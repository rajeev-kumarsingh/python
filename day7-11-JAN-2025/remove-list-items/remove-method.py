"""
The remove() method in Python can be used in DevOps scenarios to dynamically remove specific elements from a list. 
It is especially helpful when managing configurations, server inventories,
 or CI/CD tasks where certain elements need to be excluded.
"""
#Scenario: Removing a Server from Inventory
#Suppose you have a list of active servers, and one of them is decommissioned or needs to be excluded.
# List of active servers
servers = ["server1.example.com", "server2.example.com","server3.example.com", "server4.example.com"]
#remove a server from the list 
servers.remove("server3.example.com")
# Post removal print the list of active servers list 
print("Active Servers: ",servers)
