# A tuple is an ordered and unchangeable collection, so we can group related data

# instead of [] as in lists we use ()

student = ("Edu", 21, "Male")

print(student)
# counts how many times a value appears
print("Edu appears " + str(student.count("Edu")) + " times")
# shows the index of desired item
print("The age is located at index " + (str(student.index(21))))
print()

# with a for loop
for i in student:
    print(i)

print()

# using if
if 21 in student:
    print("Student is allowed to drink")
