"""
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""
# 1. Updating Configuration Management Files
#You might receive additional configuration options as a set and append them to a list of current configurations.
# Existing configuration options
config_options = ["enabled_login=true", "retry_attempts=3"]
# new options received as a set
new_config = {"use_tls=true", "timeout=30"}
#Extend the list with the set 
config_options.extend(new_config)
#print the extended list with set 
print("Extended list with set: ",config_options)

#2. Combining Kubernetes Pod Names from Different Clusters
#You could combine pod names from different clusters for reporting purposes.
# Pods in cluster A
cluster_a_pods = ["nginx-pod", "redis-pod"]
# Pods in cluster B (provided as a string, e.g., from an API response)
cluster_b_pods = ("mongodb-pod", "rabbitmq-pod")
#Combine Pod list 
cluster_a_pods.extend(cluster_b_pods)
# Print Extended pods (list with string)
print("All Pods: ", cluster_a_pods)