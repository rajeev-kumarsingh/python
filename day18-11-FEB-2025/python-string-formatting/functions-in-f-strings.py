# Functions in F-strings
def calculator(num1, num2):

  #num1 = float(input("Enter 1st number: "))
  #num2 = float(input("Enter 2nd number: "))
  addition = f"Addition of {num1} and {num2} is {num1 + num2}"
  multiplication = f"Multiplication of {num1} and {num2} is { num1 * num2}"
  division = f"Division of {num1} and {num2} is {num1/num2}" if num2!= 0 else "Division by 0 is not allowed" 
  subtraction = f"subtraction of {num1} and {num2} is {num1 - num2}" if num1 >num2 else f"Subtraction of {num2} and {num1} is {num2 - num1}" 
  return f"\n{addition}\n{multiplication}\n{division}\n{subtraction}"

# Now we will above finction in f-string

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
result = f"Mathmatical Operations :\n {calculator(num1,num2)}"
print(result)
