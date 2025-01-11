"""Scenario: Restarting a List of Servers
Suppose you have a list of server names, and you need to loop through them to restart each one."""
# list of severs
servers = ["server1.example.com", "server2.example.com", "server3.example.com", "server4.example.com"]

#Loop through the servers and restart each
for server in servers:
  print(f"Restarting {server}....")
  #Placeholder for the restart command (e.g., SSH, API CALL)
  print(f"{server} restarted successfully")
