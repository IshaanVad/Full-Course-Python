name = input("What is your name? ") # automatically casted to a String
age = int(input("How old are you? ")) # casted to an int
height = float(input("How tall are you in cm? ")) # casted to a float

print("Hello " + name) # name is a String already
print("You are " + str(age) + " years old")
print("You are " + str(height) + "cm tall")