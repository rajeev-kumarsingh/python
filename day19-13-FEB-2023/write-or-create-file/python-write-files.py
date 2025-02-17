'''
To write to an existing file, you must add a parameter to the
open() function
"a" - Append -will append to the end of the file
"w" -Write - will overwrite any existing content
'''
# Open and read the file before writing
f = open("./write-or-create-file/demofile3.txt", "r")
print(f.read())
f.close()


f = open("./write-or-create-file/demofile3.txt", "w")
f.write("Woops, I have deleted the content!")
f.close()

# Open and read the file afer writing
f = open("./write-or-create-file/demofile3.txt", "r")
print(f.read())
f.close()

