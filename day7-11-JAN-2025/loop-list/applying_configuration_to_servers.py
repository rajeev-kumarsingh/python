"""Apllying configurations to servers
You can loop through a list of servers and apply configurations using tools like Ansible or SSH commands.
"""
# Servers list
servers = ["server1.example.com","server2.example.com","server3.example.com","server4.example.com"]

#Loop through the server and apply configuration
for server in servers:
  print(f"Applying configuration to {server}.....")
  #Replace with the actual command or function
  print(f"Configuration applied to {server}")
  