"""
F-String placeholder- {} with function
"""

def greet(name):
  return f"Hello {name}"

name = "Rajeev"
message = f'{greet(name)}'
print(message)

number = 5000
def multiply(num):
  return num * 2

fstringPlaceholderwithFunction = f"The Price is {multiply(number)} INR"
print(fstringPlaceholderwithFunction) # Returns The price is 10000


def message():
  print ("I am a function, edit me to do operations instead of this message")

fstringPlaceholderwithFunction1 = f"{message()}" # Returns I am a function, edit me to do operations instead of this message

