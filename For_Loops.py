# for loop = a statement that will execute it's block of code
#            a limited amount of times
#            EXCLUDES END VALUE IN A LOOP
#
#            while loop = unlimited
#            for loop = limited

for i in range(10): # i = 0,1,2,3,4,5,6,7,8,9
    print(i+1) # prints the values 1 through 10
    
for i in range(50, 100+1, 2): # prints the values between 50 through 100, by 2
    print(i)
    
for i in "Bro Code": # prints the character in the String
    print(i)
    
for x in range(10, 0, -1): # countdown from 10 to 0
    print(x)