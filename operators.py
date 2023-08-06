#Operators are used to perform operations on variables and values.
x = 2
y = 5
#**	Exponentiation	x ** y
print(x ** y) #same as 2*2*2*2*2
#otput >32

x = 5
y = 2
#%	Modulus	x % y
print(x % y)
#otput >1

x = 15
y = 2

print(x // y) #otput >7

#the floor division // rounds the result down to the nearest whole number

#Assignment operators are used to assign values to variables:
#Comparison operators are used to compare two values:
#Logical operators are used to combine conditional statements:
x = 5
#and
print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5
#or
print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result

#Operator precedence describes the order in which operations are performed.
print((6 + 3) - (6 + 3))
"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
