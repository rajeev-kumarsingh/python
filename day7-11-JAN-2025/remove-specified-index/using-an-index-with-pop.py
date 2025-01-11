"""
Using an index with pop(). ex- pop(1) pop(0) pop(n),  n= 0,1,2,3,......(positive and negative integers)
You can also specify an index to remove and retrieve a specific element.
"""
#List of active servers
servers = list(("server1.example.com","server2.example.com", "server3.example.com", "server4.example.com"))

#Remove inactive server 
inactive_server = servers.pop(0) #or servers.pop(1)/severs.pop(2)

print("Server Removed: ", inactive_server)
print("Remaining Servers: ", servers)

inactive_server2 = servers.pop(-1)

print("Server Removed: ", inactive_server2)
print("Remaining Servers: ", servers)


