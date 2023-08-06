x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
print(type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a) #1.0
print(b) #2
print(c) #(1+0j)

print(type(a))
print(type(b))
print(type(c))
#Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

#output is 1
