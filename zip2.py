
students = ["Harry", "Ron", "Hermione", "Draco", "Neville", "Voldemort"]
grades = [99, 98, 97, 96, 95, 94]
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

for student, grade, color in zip(students, grades, colors):
    print(f"{student}: {grade}, {color}")

report_card = zip(students, grades, colors)

# print(list(zip(students, grades)))
# print(report_card)
print(list(report_card))