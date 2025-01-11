"""
Managing CI/CD Pipeline Stages
In a CI/CD pipeline, you may want to dynamically remove and execute stages in order.
"""
#list of pipeline stages
pipeline_stages = ["Checkout Code", "Build Artifact", "Run Test", "Deploy"]
#Remove and execute the last stage 
current_stage = pipeline_stages.pop()

print("Executing stage: ", current_stage)
print("Remaining Stages: ", pipeline_stages)
