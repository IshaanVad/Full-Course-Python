# slicing  = create a substring by extracting elements from another string
#            indexing[] or slice()
#            [start:stop:step]

name = "Bro Code"

first_name = name[:3] # same as [0:3]
last_name = name[4:] # same as [4:end]
funky_name = name[::2] # same as [0:end:2], where last number is incrementation
reversed_name = name[::-1] # same as [0:end:-1]

print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4) # grabs "google", the -4 goes backwards and removes the ".com"
print(website1[slice])
print(website2[slice])