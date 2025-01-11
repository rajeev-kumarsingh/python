"""
3. Handling Kubernetes Pods
You might use pop() to remove and monitor pods from a list as they get terminated.

"""
# List of active pods 
pods = ["nginx-pod", "redis-pod", "mongodb-pod"]

#Remove and retrive the last pod
terminated_pods = pods.pop()

print("Terminated Pod: ", terminated_pods)
print("Remaining Pods: ", pods)
