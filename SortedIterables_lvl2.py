
#* sort() method is used with lists
#* sort() function is used with iterables

students = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 29),
    ("Spongebob", "B", 21),
    ("Mr. Krabs", "C", 61)
    ]

students.sort() #sorts by 1st column b default

for i in students: 
    print(i)

print()
print("Sorted by grades →")

sorted_students = students
grade = lambda grades:grades[1] # → use 2 to sort by age
sorted_students.sort(key = grade)

for i in sorted_students:
    print(i)

print()
print("Sorted by grades, only reversed →")

sorted_students.sort(key = grade, reverse=True)

for i in sorted_students:
    print(i)