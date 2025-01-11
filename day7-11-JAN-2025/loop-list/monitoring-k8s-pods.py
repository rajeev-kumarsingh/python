"""2. Monitoring Kubernetes Pods
Loop through a list of pods to check their status."""

#list of pods 
pods = ["nginx-pod", "redis-pod", "mongodb-pod", "rabbitdb-pod"]

# Loop throgh the pods and check their status 
# or monitor the status of each pod
for pod in pods:
  print(f"Checking status of {pod}......")
  # Replace the actual monitoring logic (e.g., kubectl or API calls )
  print(f"{pod} is running! \n")

