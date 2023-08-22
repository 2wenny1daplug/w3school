"""Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates"""

#Dictionaries are written with curly brackets, and have keys and values:

#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#output > {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

"""Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name."""

#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#output > Ford

#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key:

#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#output > {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#To determine how many items a dictionary has, use the len() function:

#Print the number of items in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

#The values in dictionary items can be of any data type:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#this dictionary contain String, int, boolean, and list data types:

#Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


"""You can access the items of a dictionary by referring to its key name, inside square brackets:"""

#Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#otput > Mustang

#There is also a method called get() that will give you the same result:

#Get the value of the "model" key:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")       # get() method

print(x)

   

"""The keys() method will return a list of all the keys in the dictionary"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)

#otput > dict_keys(['brand', 'model', 'year'])

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change    #output > dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change     #output > dict_keys(['brand', 'model', 'year', 'color'])


"""The values() method will return a list of all the values in the dictionary"""

#Get a list of the values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x) #output > dict_values(['Ford', 'Mustang', 1964])
"""The list of the values is a view of the dictionary, 
meaning that any changes done to the dictionary will be reflected in the values list"""
ord
#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values() 
print(x) #output > dict_values(['Ford', 'Mustang', 1964])    before the change

car["year"] = 2020

print(x) #output > dict_values(['Ford', 'Mustang', 2020])    after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
 
print(x)   #output > dict_values(['Ford', 'Mustang', 1964])    before the change
 
car["color"] = "red"

print(x)  #output > dict_values(['Ford', 'Mustang', 'red'])    after the change























