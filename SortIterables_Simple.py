# * sort() method is used with lists
# * sort() function is used with iterables
# does not work with tuples

students = ["Squidward", "Sandy", "Patrick", "SpongeBob", "Mr. Krabs"]

students.sort()

print("Student list in alphabetical order →")
for i in students:
    print(i)

print()

print("Reversed student list →")
students.sort(reverse=True)

for i in students:
    print(i)

print()

print("Working with tuples →")

sorted_students = sorted(students)

for i in sorted_students:
    print(i)

print()

reversed_students = sorted(students, reverse=True)

print("Reversed student tuple →")

for i in sorted_students:
    print(i)

print()
