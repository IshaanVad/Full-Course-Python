# logical operators = "and", "or", "not"

temp = int(input("What's the temperature outside?"))

if (temp >= 0 and temp <= 30): # java: &&
    print("the temperature is good today!\ngo outside")
elif (temp < 0 or temp > 30): # or: ||
    print("the temperature is bad today!\nstay inside!")