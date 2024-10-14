
# Create a dictionary to store student grades for different subjects
student_grades = {}

# try to add a grade for 'math' for a student named 'Alice' using .get()
math_grade = student_grades.get('Alice', {})
print(student_grades)

# Now try to add a grade for 'English' for 'Alice' using .setdefault()
english_grade = student_grades.setdefault('Alice', {})
english_grade['English'] = 90
print(student_grades) # prints {'Alice': {'English': 90}