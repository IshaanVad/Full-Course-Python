# indexing operator [] = gives access to a sequence's element (str, list, tuples)

name = "bro Code!"

if (name[0].islower()): # if first index of String is lowercase
    name = name.capitalize()
    
first_name = name[:3].upper() # from start to 3rd index, make all letters uppercase
last_name = name[4:].lower() # from 4th index to end, lower case all letters
last_character = name[-1] # get last character

print(first_name)
print(last_name)
print(last_character)