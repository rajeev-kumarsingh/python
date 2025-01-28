'''
Information can be passed into functions as arguments.

Arguments are specified after the function name, 
inside the parentheses.
 You can add as many arguments as you want, 
 just separate them with a comma.
'''
'''
def my_fun(fname):{
  print("Welcome", fname,"to the python function class")

}
  
my_fun("Rajeev")
my_fun("Shiva")

'''
'''
def add_function(first, second):
  {
    print("Addition of your passed arguments is :", first +second )
  }
add_function(5,5)
add_function(55,55)
'''
'''

def display_name(fname, lname):
  {
    print("Hello", fname, "", lname)
  }
display_name("Rajeev")
'''
'''

# If the number of arguments is unknown, add a * before the parameter name:
def display_name(*name):
  print("Your fav fruit is: ", name[1])
  print("Your fav fruit is: ", name)
  print("Your fav fruit is: ", name[0])
display_name("Apple","Mango","Kiwi", "Banana")
'''

'''

## Keyword Arguments

def fruits(first,second,third,fourth,fifth):
  {
    print("My fav fruit is: ",fifth )
    
  }
fruits(first="Apple", second="Banana", third="Guava", fourth="Mango", fifth="Kiwi")

'''

'''

### Example: If the number of keyword arguments is unknown, add a double ** before the parameter name:
def all_name(**name):
  {
    print("First name is: ", name["fname"])
  }
all_name(fname = "Rajeev", lname="Singh", mname="Kumar")
'''

## Default Parameter Value
# If we call the function without argument, it uses the default value:

def default_parameter_example(country = "India"):
  {
    print("I am from ", country)

  }
default_parameter_example("Dubai")
default_parameter_example("America")
default_parameter_example("India")
default_parameter_example()
default_parameter_example("Switzerland")