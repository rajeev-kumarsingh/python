'''
To create a new file in Python, use the open() method, 
with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists

'''
# Create a file called myfile
f = open("./write-or-create-file/myfile", "x")
# write the content in myfile
f = open("./write-or-create-file/myfile", "w")
f.write("Hi There, My name is Rajeev Kumar Singh ")
f.close()

# Read the file after creating file and writing content 
f = open("./write-or-create-file/myfile", "r")
print(f.read())
f.close()
