
#? Task 1 → create a function that calculates average marks
#? Task 2 → create a function that returns the grade based on marks

#* grading rules: 
# A → equal or above 80
# B → equal or above 60 and less than 80
# C → equal or above 50 and less than 60
# D → less than 50

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_of_marks = len(marks)
    average_marks = sum_of_marks / total_of_marks
    
    return average_marks

def define_grade(average_marks):
    
    if average_marks >= 80:
        return "A"
    
    elif average_marks >= 60 and average_marks < 80:
        return "B"
    
    elif average_marks >= 50 and average_marks < 60:
        return "C"
    
    else:
        return "F"


marks = (50, 78, 90, 55, 75)
my_average_marks = find_average_marks(marks)
my_grade = define_grade(my_average_marks)

print(my_average_marks)
print(my_grade)


#? LAMBDA FUNCTIONS are written in one line using the lambda keyword
#?  → they accept any number or arguments, but only have one expression

#* FORMULA → lambda parameter: expression

double = lambda x: x * 2
# nearly the same as:
# def double(x):
#   return x * 2

print(double(5))
print()

multiply = lambda x, y: x * y
print(multiply(10,11))
print()

full_name = lambda first_name, last_name: first_name.capitalize() + " " + last_name.capitalize()
print(full_name("edu", "Vieira"))
print()

# Filtering out only the even items from a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print("Original list:", my_list)
print("Even numbers:", new_list)
print()

# Doubling each item in a list using map()

new_list2 = list(map(lambda x: x * 2, my_list))
print("Original list:", my_list)
print("Doubled:", new_list2)


