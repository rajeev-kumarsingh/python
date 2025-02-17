# open() function with read() method
f = open("./read-files/demofile.txt","r")
#print(f.read())
#print("\n")
# Return the 6 first characters of the file:
#print(f.read(5))

#print(f.readline())
#print(f.readline())
for x in f:
  print(x)
f.close()
