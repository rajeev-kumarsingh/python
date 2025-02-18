'''
To delete an entire folder, use the os.rmdir() method:

'''
import os
# To delete an entire folder, use the os.rmdir() method:
if os.path.exists("./delete-files/test-folder"):
  os.rmdir("./delete-files/test-folder")
else:
  print("The folder is not exist")
