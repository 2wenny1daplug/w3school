#A set is a collection which is both unordered and unindexed.
#Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Sets are unordered, so you cannot be sure in which order the items will appear.
"""Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key"""

#sets cannot have two items with the same value

#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#output > {'banana', 'cherry', 'apple'}

#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}                  #set items can be of any data type
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

set1 = {"abc", 34, True, 40, "male"}  # a set can contain different data types

#What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

#Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

## Note: the set list is unordered, so the result will display the items in a random order.

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#output      apple
#            banana
#            cherry

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#output > True

#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#To add items from another set into the current set, use the update() method.

#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) #output > {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#output > {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#to remove an itme in a set, use remove() or discard() method

#Remove "banana" by using the remove() method

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #also u can use discard()

print(thisset)

#If the item to remove does not exist, discard() will NOT raise an error, whereas remove() will raise an error

"""You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
The return value of the pop() method is the removed item."""

#Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) # removed item                    output > cherry

print(thisset)  #the set after removal     output > {'banana', 'apple'}

#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)    #output > set()

#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)#this will raise an error because the set no longer exists

#You can loop through the set items by using a for loop:

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#output   >      cherry
#                banana
#                apple

"""You can use the union() method that returns a new set containing all items from both sets, 
or the update() method that inserts all the items from one set into another"""

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#output > {'b', 3, 1, 2, 'c', 'a'}

#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#output > {1, 3, 2, 'a', 'b', 'c'}

# Both union() and update() will exclude any duplicate items.


"""The intersection_update() method will keep only the items that are present in both sets."""

#Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#output > {'apple'}


#Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection_update(y)

print(z) #output > {'apple'}


""" the symmetric_difference_update() method keeps the elements that are NOT present in both sets"""
#Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference_update(y)

print(z)

#output > {'google', 'banana', 'microsoft', 'cherry'}



































