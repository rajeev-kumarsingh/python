"""
By leaving out the start index, The range will start at the first character.
"""
s = "Get-the-characters-from-the-start-to-position-5(not-included)"
print("Given String is: ",s)
print("Number of characters: ",len(s))
print(s[:5])
print(s[:10])
print(s[:20])
print(s[:30])
print(s[:50])
print(s[:61])

print("start to 5 ",s[:5])
print("Start to 10 ",s[:10])
print("Start to 20 ",s[:20])
print("Start to 30 ",s[:30])
print("Start to 50 ",s[:50])
print("Start to 61",s[:61])
