"""
remove() -Practical Use Cases in DevOps

"""
"""Removing failed CI/CD stages 
In a CI/CD pipeline, if a particular stage fails, 
you may need to remove it dynamically from a list of stages to reconfigure the pipeline.
"""
#list of pipeline stages 
pipeline_stages = ["Checkout Code", "Build Artifact", "Run Tests", "Deploy" ]
#Remove a failed stage 
pipeline_stages.remove("Run Tests")
print("Updated Pipeline Stages: ", pipeline_stages)