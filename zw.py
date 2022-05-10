
#? Functions

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))

id = 240
student_name = []
student_age = []
student_course = []
student_id =[]

def enroll():
    num = int(input("How many students are you enrolling? "))
        
    for i in range(1, num + 1):
        student_name.append(input("Name: "))
        student_age.append(input("Age: "))
        student_course.append(input("Course: "))
        student_id.append(id + i)
        print()

def report():
    print("Students enrolled today →")
    print("--------------------------------------------------------------------")
    
    for i in range(0, len(student_id)):
        
        print("Student id → " + str(student_id[i]) + ", name: "
              + str(student_name[i]) + ", " + str(student_age[i]) + " attending the "
              + str(student_course[i]) + " course.")
        print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        
enroll()
report()