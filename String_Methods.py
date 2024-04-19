name = "bro"

print(len(name)) # length of string
print(name.find("o")) # finds index of letter (0-based indexing), returns -1 if no in string
print(name.capitalize()) # capitalizes first letter in string
print(name.upper()) # capitalizes every letter in string
print(name.lower()) # lowercases every letter in string
print(name.isdigit()) # true or false if string is a number
print(name.isalpha()) # true or false if all characters are letters
print(name.count("o")) # returns number of certain letter(s) within string
print(name.replace("o", "a")) # replaces letter within string with desired letter
print(name * 3) # repeats string as many times as desired