# a = "Whats"
# b = "cookin"
# c = "good-lookin"
# d = a + " " + b + " " + c
# print(d)


# NOT WORKING ### Try It Out!
# Given the following list: `myList = [23,45,12,10,25]`, find the sum of the numbers using a `while` loop.

# myList = [23,45,12,10,25]
# i=0
# sum=0
# while i < len(myList):
#     sum += myList[i]
#     i=i+1  
# print(sum)    

# myList = [23,45,12,10,25]
# i=0
# sum=0
# while i < len(myList):
#     sum+=myList[i]
#     i=i+1
# print(sum)

# it works ### Try It Out!
# Print the following lists as a 2D array: `list1 = [5,10,15,20]` `list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']`
# Hint: nested loops

# list1 = [5,10,15,20]
# list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

# for x in list1:
#     for y in list2:
#         print(x,y)

# It Works ### Try It Out!
# Given the following list: `vehicles = ['Car','Cycle','Bus','Tempo']`, print the values until you reach `Bus`.
# Hint: break out of the list

# vehicles = ['Car','Cycle','Bus','Tempo']

# for x in vehicles:
#     print(x)
#     if x == "Bus":
#         break

# I HAVE NO IDEA ON THIS ONE ### Try It Out!
# Using the same list from the previous exercise: `vehicles = ['Car','Cycle','Bus','Tempo']`, print the values and skip the `Bus` element.
# Hint: continue printing the rest of the list

# vehicles = ['Car','Cycle','Bus','Tempo']

# for vehicles    in vehicles:
#     if vehicles == "Bus":
#         continue
        
#     print(vehicles)

# Its not working ### Try It Out!
# Take as input the age of 3 people, and determine oldest and youngest among them.

ppl = ("erin", "Diana", "Danny", "Maggie")
(42, 39, 36, 32) = ppl.int

print("\nTuple packing ...")
print(42 =, "42", 39 =, "39", 36 =, "36", 32 =, "32")




# # Packing a Tuple
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits

# print("\nTuple packing ...")
# print("green=", green, "yellow=", yellow, "red=", red)


#LIndsey did in class### Try It Out!
# A school has the following rules for their grading system:
# - a. Below 25 - F
# - b. 25 to 45 - E
# - c. 45 to 50 - D
# - d. 50 to 60 - C
# - e. 60 to 80 - B
# - f. Above 80 - A

# Ask the user to input the score they received for a class and print the corresponding grade.