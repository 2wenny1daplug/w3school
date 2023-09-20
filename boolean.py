a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#b is not greater than a

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#output > False

#You can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())
#otput > True

#You can execute code based on the Boolean answer of a function:
#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#otput > YES!

#Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:

#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

#otput > True
