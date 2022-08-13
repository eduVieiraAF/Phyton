# ? List comprehension is a wa to create a new list with less syntax
#        can mimic certain lambda functions, and it's easier to read
#        list = [expression for item in iterable]
#        list = [expression for item in iterable if conditional]
#        list = [expression if/else conditional for item in iterable]

# ! Big syntax
# squares = [] # empty list
# for i in range(1,11):
#     squares.append(i * i) 

# print(squares)

squares = [i * i for i in range(1, 11)]

print(squares)
print()

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# using filter()
# failed_students = list(filter(lambda x: x <= 60, students))

failed_students = [i for i in students if i <= 60]

passed_students = [i if i >= 60 else "FAILED" for i in students]

print(failed_students)
print(passed_students)
