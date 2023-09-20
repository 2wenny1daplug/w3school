#store multiple items in a single variable, 
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#to create a tuple with only one item, you have to add  comma after he item.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)                #Tuple items can be of any data type:
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male") #A tuple can contain different data types:

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #They are defined as objects with the data type 'tuple':

#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #output > banana

#Print the last item of the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #output > cherry

#When specifying a range, the return value will be a new tuple with the specified items.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).
#Remember that the first item has index 0.

#This example returns the items from the beginning to, but NOT included, "kiwi"
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

#To determine if a specified item is present in a tuple use the in keyword:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#tuples are immutable
#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#output > ('apple', 'banana', 'cherry', 'orange')

#Create a new tuple with the value "orange", and add that tuple:

thistuple =  ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #output > ('apple', 'banana', 'cherry', 'orange')

#You cannot remove items in a tuple.

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#you can delete a tuple completely by using the del keyword

thistuple = ("apple", "banana", "cherry") #packing a tuple/when we assign a value to it
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

"""If the number of variables is less than the number of values, you can add an * 
to the variable name and the values will be assigned to the variable as a list:"""
#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)   #apple
print(yellow)  #banana
print(red)     #['cherry', 'strawberry', 'rasberry']

"""If the asterisk is added to another variable name than the last, Python 
will assign values to the variable until the number of values left matches the number of variables left"""

#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)  # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red)    # cherry

#You can loop through the tuple items by using a for loop.

#Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#output       apple
#             banana
#             cherry

"""You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable."""

#Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#output            apple
#                  banana
#                  cherry

"""You can loop through the list items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
Remember to increase the index by 1 after each iteration."""

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#output            apple
#                  banana
#                  cherry

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
#To join two or more tuples you can use the + operator:
tuple3 = tuple1 + tuple2
print(tuple3)

#output > ('a', 'b', 'c', 1, 2, 3)

#Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#('apple', 'banana', 'cherry','apple', 'banana', 'cherry')































