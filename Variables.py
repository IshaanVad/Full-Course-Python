# String
first_name = "Bro"
last_name = "Code"
full_name = first_name + " " + last_name
print("Hello " + full_name)

print(type(first_name)) # check datatype of var

print() # new line

# int - whole number
age = 21
age += 1
print(age)
print(type(age))

print("your age is " + str(age)) # must type case int to String literal


print()

# float - decimal number
height  = 250.5
print(height)
print(type(height))

print("Your height is " + str(height) + "cm") # must type case float to String literal

print()

# boolean - true or false
human = False
print(human)
print(type(human))

print("Are you a human? " + str(human))

# multiple assignment = allows us to assign multiple variables at the same time in one line of code

# x = "Name"
# y = 30
# attractive = True

# instead
name, age, attractive = "Name", 30, True

# what if different vars but same value
Spongebob = 30
Patrick = 30
Squidward = 30

Spongebob = Patrick = Squidward = 30