'''
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
Any argument with *, are positional argument, and any argument with **, are keyword argument

'''
def my_fun(a,b,/,*,c,d):
  print(a+b+c+d)
my_fun(1,2,c=3,d=4)
print("\n")
def flexible_function(*args, **kwargs):
  print("Positional Arguments: ", args)
  print("Keyword Arguments: ", kwargs)
flexible_function("rajeev","name='rajeev'", 5, age=5)
flexible_function("rajeev","name='rajeev'", 5, age=5,name="rajeev")
print("\n")
def flexible_function(args,/, **kwargs):
  print("Positional Arguments: ", args)
  print("Keyword Arguments: ", kwargs)
flexible_function("rajeev","name='rajeev'", 5, age=5)
flexible_function("rajeev","name='rajeev'", 5, age=5,name="rajeev")

