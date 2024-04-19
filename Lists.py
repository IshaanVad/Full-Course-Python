# list = used to store multiple items in a single variable (like array lists)

food = ["pizza", "hamburgber", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi" # replaces "pizza" with "sushi", at index 0

food.append("ice cream") # adds "ice cream" to end of list
food.remove("hotdog") # remove "hotdog" from list
food.pop() # removes and returns last element
food.insert(0, "cake") # inserts item at specific index
food.sort() # sort alphabetically
#food.clear() # clears list

for x in food:
    print(x)