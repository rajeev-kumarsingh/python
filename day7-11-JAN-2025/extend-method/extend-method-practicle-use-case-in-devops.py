"""
Practical Use Case in DevOps:
1.Kubernetes Pod Management: You can extend a list of currently active pods with newly created pods.
2.Jenkins Build Tasks: If you're managing Jenkins pipeline steps programmatically, 
  you can extend an existing list of tasks with additional ones.
"""
#1. Kubernetes Pod management: Extend a list of currently active pods with newly created pods.
# Current list of active pods
active_pods = ["nginx-pod", "redis-pod"]
# List of new pods
new_pods = ['mongodb-pod', 'rabbitmq-pod']
# Extended list of active pods 
active_pods.extend(new_pods)
# Print extended list of active pods 
print("Extended list of active pods: ",active_pods)

#2. Jenkins Build Tasks: If you're managing Jenkins pipeline steps programmatically,
# you can ectend an existinf list of tasks with additional ones.
pipeline_steps = ["checkout-code", "build-artifacts"]
additional_steps = ["Run Tests", "Deploy to staging"]
pipeline_steps.extend(additional_steps)
# Updated jenkins pipeline steps
print("Updated jenkins pipeline steps: ", pipeline_steps)
