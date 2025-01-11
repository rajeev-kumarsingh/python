"""
Practical Use Case in DevOps:
You might use insert() to manage task sequences in tools like Jenkins pipelines, update server inventories, 
or control the order of operations in a configuration management script.
"""
#For instance:
#List of server 
server = ["server1.example.com", "server3.example.com"]
print("List of server is: ", server)
priority_server = "server2.example.com"
# insert the priority server at the beginning of the list
server.insert(0, priority_server)
# Print the updated list of server
print("Updated server list: ", server)
