#ists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#output >['apple', 'banana', 'cherry']
"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc."""
#If you add new items to a list, the new items will be placed at the end of the list.
#Note: There are some list methods that will change the order, but in general: the order of the items will not change.
#Since lists are indexed, lists can have items with the same value:

#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#output > 3

#List items can be of any data type:
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)
#output >['abc', 34, True, 40, 'male']

#From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>

#What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#output ><class 'list'>

#It is also possible to use the list() constructor when creating a new list.
#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#['apple', 'banana', 'cherry']

"""
There are four collection data types in the Python programming language:

List-is a collection which is ordered and changeable. Allows duplicate members.
Tuple-is a collection which is ordered and unchangeable. Allows duplicate members.
Set is-a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
#*Set items are unchangeable, but you can remove and/or add items whenever you like.

#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#output > banana
#Note: The first item has index 0.
"""
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc."""

#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#otput > cherry
"""You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items."""

#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']

#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#Note: The search will start at index 2 (included) and end at index 5 (not included).


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

#This example returns the items from the beginning to, but NOT including, "kiwi":
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

#By leaving out the end value, the range will go on to the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#output > ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#Specify negative indexes if you want to start the search from the end of the list:
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #otput > ['orange', 'kiwi', 'melon']

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

#To determine if a specified item is present in a list use the in keyword:

#Check if "apple" is present in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") # Yes, 'apple' is in the fruits list

#To change the value of a specific item, refer to the index number:

#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #otput > ['apple', 'blackcurrant', 'cherry']

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) 
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
"""If you insert more items than you replace, the new items 
will be inserted where you specified, and the remaining items will move accordingly:"""

#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']
#Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#otput > ['apple', 'watermelon']

"""To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:"""
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #output > ['apple', 'banana', 'watermelon', 'cherry']

#Note: As a result of the example above, the list will now contain 4 items.

#To add an item to the end of the list, use the append() method:
#Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#To append elements from another list to the current list, use the extend() method.
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

#The remove() method removes the specified item.
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #output > ['apple', 'cherry']

#The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #output > ['apple', 'cherry']

#Note If you do not specify the index, the pop() method removes the last item.
#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']

#The del keyword also removes the specified index:
#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #output > ['banana', 'cherry']

#The del keyword can also delete the list completely.
#Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

#The clear() method empties the list.the list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()  #Clears the list content:
print(thislist) #output > []

#You can loop through the list items by using a for loop:
#PrintS all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

"""You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable."""

#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) #apple
#                     banana
#                     cherry


#The iterable created in the example above is [0, 1, 2].
"""You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
remember to increase the index by 1 after each iteration."""

#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"] #List comprehension
[print(x) for x in thislist] 
"""Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #output > ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) #output > ['apple', 'banana', 'mango']

#newlist = [expression for item in iterable if condition == True]   the syntax
#The return value is a new list, leaving the old list unchanged.
#The condition is like a filter that only accepts the items that valuate to True.

#Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"] 
print(newlist) #Output > ['banana', 'cherry', 'kiwi', 'mango'] 

"""The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
The condition is optional and can be omitted:"""
 
#With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist) #output > ['apple', 'banana', 'cherry', 'kiwi', 'mango']

#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

print(newlist) #output > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

print(newlist) #output > [0, 1, 2, 3, 4]

#Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist) #output > ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#You can set the outcome to whatever you like:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist) #output > ['hello', 'hello', 'hello', 'hello', 'hello']

#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
#the expression above says "Return the item if it is not banana, if it is banana return orange".

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #Sorts the list descending:
print(thislist)

"""You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):"""

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #output > [50, 65, 23, 82, 100]

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #output > ['Kiwi', 'Orange', 'banana', 'cherry']

# if you want a case-insensitive sort function, use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#output > ['banana', 'cherry', 'Kiwi', 'Orange']

#The reverse() method reverses the current sorting order of the elements regarless of the alphabet

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # otput > ['cherry', 'Kiwi', 'Orange', 'banana']

"""You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2"""
#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#output > ['apple', 'banana', 'cherry']

#Another way to make a copy is to use the built-in method list().
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#joining two lists/concatenation

#join two list using the + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Print the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.

fruits = ["apple" , "banana" , "cherry"]
fruits[0] = "kiwi"

#Use the append method to add "orange" to the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Use the insert method to add "lemon" as the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#Use the remove method to remove "banana" from the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Use negative indexing to print the last item in the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the list.

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Use the correct syntax to print the number of items in the list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Use the correct syntax to print the first item in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Use the correct syntax to print the number of items in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is afruit!")

#Use the add method to add "orange" to the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")


