import json
# Order the Result
x = {
  "name": "Rajeev",
  "age": 30,
  "employed": True,
  "married": False,
  "books": ("Linux","javascript"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys= True )
print(type(y))
print(y)