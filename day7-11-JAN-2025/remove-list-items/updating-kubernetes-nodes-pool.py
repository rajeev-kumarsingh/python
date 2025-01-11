"""
2. Updating Kubernetes Node Pool

"""
"""
If a specific kubernetes node is unhealthy, you can remove it from the node pool list.
"""
#list of nodes in kubernetes cluster
k8s_nodes = ["node1", "node2", "node3", "node4", "node5"]
#remove unhealthy node 
unhealthy_node = "node3"
if unhealthy_node in k8s_nodes:
  k8s_nodes.remove("node2")

print("Updated k8s nodes: ", k8s_nodes)

