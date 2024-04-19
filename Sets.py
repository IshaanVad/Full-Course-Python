# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin") # adds item to set 
utensils.remove("fork") # removes object within set
utensils.clear() # clears set
dishes.update(utensils) # adds other set to this set
dinner_table = utensils.union(dishes) # .union() returns a new set with distinct elements from all sets

print(dishes.difference(utensils)) # returns different elements in the sets
print(utensils.intersection(dishes)) # returns common elements within the sets

for x in dinner_table:
    print(x)