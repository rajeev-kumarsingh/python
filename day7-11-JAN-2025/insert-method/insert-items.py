"""
Insert Items: To insert a list item at a specified index, use the insert() method.
The insert() method allows you to add an item to a specific position in a list.
"""
#Example: Using insert() to Manage a Deployment Pipeline
# Suppose you are managing a list of deployment stages in a devops pipeline, and you need to add a new stage at a 
#specific podition in the pipeline 
# list of deployment stages 
deployment_pipeline = ["Build", "Test", "Deploy"]
# Insert a new stage "Code Analysis ", before test.
deployment_pipeline.insert(1,"Code Analysis")
# Print the updated pipeline
print("Updated Pipeline is: ", deployment_pipeline)
 