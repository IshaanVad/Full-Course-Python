# function = a block of code which is executed only when it's called
#            MUST BE DEFINED BEFORE IT IS USED (so like at the top of the class), before being called

def helloWorld():
    print("Hello World!")

def hello(first_name, last_name, age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day")
    
# return statement
def multiply(number1, number2):
    return number1 * number2

helloWorld()
print()
hello("Bro", "Code", 21)
print()
x = multiply(2, 3)
print(x)