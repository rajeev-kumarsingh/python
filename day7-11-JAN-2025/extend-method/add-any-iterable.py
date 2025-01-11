"""
In Python, the extend() method can be used to add any iterable (like a list, tuple, set, or even a string)
 to an existing list.
 This feature can be quite helpful in various DevOps scenarios, especially for dynamically updating configurations 
 or inventories.
"""
# Example: Adding Any Iterable in DevOps
#Scenario: Updating a List of Environment Variables
"""
Suppose you have a list of default environment variables for a container, and 
you need to add more variables (provided as a tuple) during runtime.
"""
# Default environment variable for a container
env_vars = ["DB_HOST=localhost", "DB_PORT=5432"]
# Additional variable provided as tuple
new_env_var = ("CACHE_ENABLED=true", "CACHE_SIZE=256MB")

# Extend the list with tuple
env_vars.extend(new_env_var)
#Print the extended list of environment variables
print("Updated Environment Variables: ", env_vars)
