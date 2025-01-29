'''
Create an iterator that returns numbers, 
starting with 1, and each sequence will increase by one
 (returning 1,2,3,4,5 etc.):

'''

'''

class myNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = myNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''

'''
In the __next__() method, 
we can add a terminating condition to raise an error 
if the iteration is done a specified number of times:


'''
class myNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 6:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = myNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
