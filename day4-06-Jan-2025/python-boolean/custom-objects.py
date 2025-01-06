#The bool() function is helpful when you need to determine whether a value is logically "true" or "false" in your code.
class MyClass:
  def __len__(self):
    return 0
  
print(bool(MyClass()))  # False (__len__() returns 0)

class AnotherClass:
  def __bool__(self):
    return True
  
print(bool(AnotherClass()))  # True (__bool__() returns True)

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

