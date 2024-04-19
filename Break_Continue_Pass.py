# Loop Control Statements = change a loops excecution from its normal sequence

# break = exits loop
# continue = moves to next index loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break
    
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue # move to next index
    print(i, end="")
    
print()
    
for i in range(1, 21):
    if i == 13:
        pass # does nothing, just a placeholder
    else:
        print(i)