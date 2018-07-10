# Create a tuple named zoo that contains your favorite animals.
zoo = ("giraffe", "zebra", "reindeer", "panther")
print("The zoo is created as a tuple", zoo)

# Find one of your animals using the .index(value) method on the tuple.
print("Index of zebra in the tuple is - ", zoo.index("zebra"))

# Determine if an animal is in your tuple by using for value in tuple.
print("Loop through the zoo animals")
for value in zoo:
    if value == "zebra":
        print("Yeah, we have zebras - ", value)
    else:
        print("This is not a zebra - ", value)

# Create a variable for each of the animals in your tuple with this cool feature of Python.
(giraffe, zebra, reindeer, panther) = zoo
print("Display the variable for giraffe - ", giraffe)

# Convert your tuple into a list.
zoo_list = list(zoo)
print("Converted zoo tuple to list", zoo_list)

# Use extend() to add three more animals to your zoo.
zoo_list.extend({"hippo", "hyena", "horse"})
print("Additional animals in the zoo", zoo_list)

# Convert the list back into a tuple.
zoo_tuple = tuple(zoo_list)
print("Put zoo back in tuple", zoo_tuple)