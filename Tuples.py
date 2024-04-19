# tuple = collection which is ordered and unchangeable
#         used to group together related data
#         (kind of like objects)

student = ("Bro", 21, "male")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Bro" in student:
    print("Bro is here!")