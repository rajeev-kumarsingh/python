'''
# Keyword-only arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
'''

'''
# keyword-only arguments
# add * before arguments
def keyword_only(*, x):
  print(x)
keyword_only(x = 3)
'''

# Without * You are only allowed to use positional arguments
def my_fun(x):
  print(x)
my_fun(5)
print("\n")
# But with the *, you will get an error if you try to send a positional argument:
def my_fun(*,x):
  print(x)
my_fun(x = 5)
my_fun(x = "Rajeev Kumar Singh")
my_fun(5)

