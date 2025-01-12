"""Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):"""
#Sort the list based on how close the number is to 50:
def myfunction(n):
  return abs(n - 50)

numberList = [100,40,30.4, 50, 14,25,76]
numberList.sort(key = myfunction)
print(numberList)

"""Output: 
python3 customize-sort-function.py
[50, 40, 30.4, 25, 76, 14, 100]"""