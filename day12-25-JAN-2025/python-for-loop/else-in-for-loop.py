'''
# Else in For Loop

## The else keyword in a for loop specifies a block of code to be executed 
when the loop is finished:

### Example: Print all numbers from 0 to 5, and print a message when the loop has ended:
'''
# Example :Print all numbers from 0 to 5 and print message when the loop has ended
'''
numbers = [10,1,25,3,444,5]
for i in range(len(numbers)):
  print(f"{i} number: {numbers[i]}")
else:
  print("Finally loop has ended!")
'''
'''
for i in range(6):
  print(i)
else:
  print("finally loop has ended")
'''

'''
Note: The else block will NOT be executed if the loop is stopped by a 
break statement

'''
for i in range(6):
  print(i)
  if i == 3:
    break
else:
  print("finally loop has ended")
