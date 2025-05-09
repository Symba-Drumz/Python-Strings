"Hello" #this is a string
'Hello' #this is also a string
greeting = "Hello" #this is storing a string in a variable



#STRING OPERATIONS
#String concatenation;
first = "Hello"
second = "world"
print(first + " " + second) #this will print Hello world

#String Length;
print(len(first)) #this will print 5. The length of the string is 5

#String indexing)getting one name);
language = "Python"
print(language[0]) #this will print P. The first letter of the string is P
print(language[1]) #this will print y. The second letter of the string is y
print(language[-1]) #this will print n. The last letter of the string is n

#String slicing(getting a piece of the string);
drummer = "Aaron"
print(drummer[0:3]) #this will print Aar. The first three letters of the string are Aar

#Finding out dunder methods;
print(dir(drummer))

#String methods;
print(drummer.upper()) #this will print AARON. The string is converted to uppercase
print(drummer.lower()) #this will print aaron. The string is converted to lowercase
print(drummer.title()) #this will print Aaron. The first letter of the string is capitalized
print(drummer.capitalize()) #this will print Aaron. The first letter of the string is capitalized
print(drummer.strip()) #this will remove any whitespace from the beginning and end of the string
print(drummer.replace("A", "B")) #this will replace A with B. The string will be Baron
#Let me try replacing more than one letter;
print(drummer.replace("A", "B").replace("r", "t")) #this will replace A with B and r with t. The string will be Baton
new_drummer = drummer.replace("A", "B").replace("r", "t") #this will replace A with B and r with t. The string will be Baton
print(new_drummer) #this will print Baton. The string is replaced with Baton
print(new_drummer.split()) #this will split the string into a list. The string will be split into a list of words
collective_drummers = "Aaron, John, Paul, Ringo"
print(collective_drummers.split(", ")) #this will split the string into a list. The string will be split into a list of words
print(collective_drummers.startswith('A')) #this will check if the string starts with A. The string starts with A
print(collective_drummers.endswith('o')) #this will check if the string ends with o. The string ends with o

#Using f-strings;
#this is a way to format strings
drummer_1 = "Aaron Spears"
drummer_2 = "Xavier Ware"
print(f"{drummer_1} is much older and more experienced than {drummer_2}.")