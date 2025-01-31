# Convert from JSON to Python:
import json

# Some JSON
details = '{"fname": "Rajeev", "mname": "Kumar", "lname":"Singh", "age": 30,"car": "none" }'

# # parse x:
x = json.loads(details)

# # the result is a Python dictionary:
print(x["fname"])
print(x["mname"])
print(x["lname"])
print(x["age"])
print(x["car"])
