x = 4      # x is of type int
x = "Sally" # x is now of type str
print(x)
"""If you want to specify the data type of a variable, 
 this can be done with casting."""
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x)) #'int'
print(type(y)) #'str'

#Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

myVariableName = "John" #Camel case
MyVariableName = "John" #Pascal case
my_variable_name = "John" #Snake case

"""
Python allows you to assign values 
to multiple variables in one line
"""
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#output is "python is awesome"

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#output is "python is awesome"
#In the print() function, when you try to combine a string
#  and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)
#Output >TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Global values 
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#Output > Python is awesome

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#Output > Python is fantastic
#         Python is awesome
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
#Output > Python is fantastic

