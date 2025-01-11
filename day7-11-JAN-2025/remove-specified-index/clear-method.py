"""
Clear the list- use clear() method
The list still remains, but it has no content.
"""
#list of kubernetes pods
pods = ["nginx-pod", "redis-pod", "mongodb-pod"]
print("List of k8s pod: ", pods)

# Clear the pod list 
pods_list_without_content = pods.clear()

print("List of k8s pod: ", pods)
print("pod list after applying clear() method: ", pods_list_without_content)
print("check type of pod_list_without_content: ", type(pods_list_without_content))
print("check type of pods: ", type(pods))

node1_pods = ["pod1", "pod2", "pod3", "pod4"]
pods.append(node1_pods)
print("Append node1_pods to pods: ", pods)
pods_list_without_content.append(pods)
print("append pods to pods_list_without_content: ", pods_list_without_content)


