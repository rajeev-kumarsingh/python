"""
Add List Items: To add an item to the end of the list, use the append() method
"""
# Here is the example of adding the item to the list in the context of DevOps
# Example: Adding an Item to a List in DevOps Automation
# List of existing server server in  the deployment
server = ["server1.example.com", "server2.example.com", "server3.example.com"]
print("Server list: ", server)
# Adding a new server to the list 
server.append("server4.example.com")
# print the updated list of server 
print("Updated server list: ", server)

"""
In devops context, you could use the similar approach to dynamically update the list of nodes in a cluster 
This could be the part of larger scripts that integrates with tools like Ansible, Terraform, or Kubernetes.
"""
#Adding a pod to a list in Kubernetes 
pods = ["nginx-pod", "redis-pod"]
new_pods = "mongodb-pod"
pods.append(new_pods)
print("Active Pods: ", pods)
