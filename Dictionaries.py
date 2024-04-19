# dictionary = a changeable, unordered collection of unique "key:value" pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # adds key:value to capitals
capitals.update({"USA":'Las Vegas'})
capitals.pop('China') # removes key:value from list
# capitals.clear() # clears dictionary

print(capitals['Germany']) # returns value of key
print(capitals.get('Germany')) # returns value of key
print(capitals.keys()) # returns keys
print(capitals.values()) # returns values
print(capitals.items()) # returns entire dictionary

for key,value in capitals.items(): # loop for key,value in dictionary
    print(key, value)
    
for value in capitals.values: # loop for value in values
    print(value)
    
for key in capitals.keys: # loop for key in keys
    print(value)