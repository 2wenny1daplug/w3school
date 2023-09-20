#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)
#You can assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Note: in the result, the line breaks are inserted at the same position as in the code.

# Python does not have a character data type,
# a single character is simply a string with a length of 1.

#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
# Output is e

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
#output  > Hello

#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
#output > llo, World

#Use negative indexes to start the slice from the end of the string:
#Get the characters:

#From: "o" in "World!" (position -5)

#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
#output orl

a = "Hello, World!"  #The upper() method returns the string in upper case:
print(a.upper())

a = "Hello, World!" # The lower() method returns the string in lower case:
print(a.lower())

a = " Hello, World! "  #The strip() method removes any whitespace from the beginning or the end:
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"    #The replace() method replaces a string with another string:
print(a.replace("H", "J")) # replaces to Jello, World!

a = "Hello, World!"
b = a.split(",")
print(b) #print(a.split(","))  # # returns ['Hello', ' World!']

#To concatenate, or combine, two strings you can use the + operator.
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c) #output HelloWorld

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

#we cannot combine strings and numbers like this:
#age = 36
#txt = "My name is John, I am " + age
#print(txt)
#But we can combine strings and numbers by using the format() method!
 
#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#otput >I want 3 pieces of item 567 for 49.95 dollars.
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #We are the so-called "Vikings" from the north.

txt = "This will insert one \\ (backslash)."
print(txt) #This will insert one \ (backslash).

txt = 'It\'s alright.' #\'	Single Quote
print(txt)  #It's alright.

txt = "Hello\nWorld!" #Hello        \n	New Line
print(txt)            #World!

#\r	Carriage Return same as newline

#This example erases one character (backspace):
txt = "Hello \bWorld!"  
print(txt) #HelloWorld