# nested loops = the "inner loop" will finish all of its iterations before finishing one interation of the "outer loop"

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "") # end = "" will prevent cursor going to next line because of print()
    print()