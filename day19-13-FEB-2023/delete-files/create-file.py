# Create a file called myfile
f = open("./delete-files/myfile", "x")
# write the content in myfile
f = open("./delete-files/myfile", "w")
f.write("Hi There, My name is Rajeev Kumar Singh ")
f.close()

# Read the file after creating file and writing content 
f = open("./delete-files/myfile", "r")
print(f.read())
f.close()