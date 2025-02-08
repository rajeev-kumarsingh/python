'''
#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try' and 'except' is finished")


try:
  print("x")
except:
  print("Nothing went wrong")
finally:
  print("The 'try' and ' except' is finished, 'try' has not raised any error ")

print("\n")
'''
#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Hello, there")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
