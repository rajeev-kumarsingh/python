"""
The pop() method in Python is useful for DevOps scenarios where you need to dynamically remove and 
retrieve an element from a list. 
This can be helpful when managing tasks, server inventories, or pipeline stages in an automated script.
"""
"""
Scenario: Removing a Server for Maintenance
Suppose you have a list of active servers, and you need to temporarily remove one for maintenance 
while also retrieving its details.
"""
#list of active servers 
servers = ["server1.example.com", "server2.example.com", "server3.example.com", "server4.example.com"]
# Remove and retrive the last server in the list
server_to_maintain = servers.pop()
print("Server taken for maintainance: ", server_to_maintain)
print("Remaining Servers", servers)
