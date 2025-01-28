'''

# Lambda function can take any number of arguments
lambda_multiArgs = lambda a,b: (a + b) * 10
print(lambda_multiArgs(10,20))
print("\n")
x = lambda a,b,c,d,e,f: ((a+b+c)*(d+e+f))/10
result = x(5,55,555,5555,55555,555555)
print(result)
'''

'''
Why use lambda function
Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number:

'''

'''

def my_fun(x):
  y=lambda a: a*55
  print(y(x))

my_fun(10)
'''

'''

# use return statement
def my_func(n):
  return lambda a: a ** n
# Use that function definition to make a function
#  that always square the number you send in:
mydoubler = my_func(2)
print(mydoubler(5))
print(mydoubler(11))
'''


# Or, use the same function definition to make both functions, in the same program:

def my_func(n):
  return lambda a: a ** n
# Use that function definition to make a function
#  that always double the number you send in:
#mydoubler = my_func(2)
#print(mydoubler(5))
#print(mydoubler(11))
print(my_func(5))


