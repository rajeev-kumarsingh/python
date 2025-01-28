'''

# Positional Only arguments
# To specify that a function can have only positional arguments, add , / 
# after the arguments:

'''
def positional_only_arguments(x, /):
  print(x)
positional_only_arguments("Rajeev Kumar Singh")
positional_only_arguments(x=5)
#positional_only_arguments(5.5)
#positional_only_arguments(True)
#positional_only_arguments(False)
