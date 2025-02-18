'''

To delete a file, you must import the OS module, 
and run its os.remove() function:

Check if File exist:
To avoid getting an error,
 you might want to check if the file exists before you try to delete it:

'''
import os
if os.path.exists("./delete-files/myfile"):
  os.remove("./delete-files/myfile")
else:
  print("The file does not exist")
  