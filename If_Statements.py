# if statement = a block of code that will execute if it's condition is true
# INDEXING MATTERS

age = int(input("How old are you? "))

if age == 100:
    print("You are old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You aren't even born yet!")
else:
    print("You are a child")