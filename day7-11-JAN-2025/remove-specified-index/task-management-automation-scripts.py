"""
Task Management in Automation Scripts
If you're managing tasks in an automation script, you can use pop() to process tasks in reverse order 
(LIFO - Last In, First Out).
"""
# List of pending tasks
tasks = ["Provision Server", "Configure Server", "Deploy Applications"]
#Process the last added task
current_task = tasks.pop()

print("Processing Task: ", current_task)
print("Remaining Tasks: ", tasks)
