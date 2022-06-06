
#* sort() method is used with lists
#* sort() function is used with iterables
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

#? Level 2

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

#* LAMBDA → lambda parameter: expression

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
    


# * starstWith() checks if a string starts with certain characters
# * endsWith() checks if as string ends with certain characters

message = "Code, drink coffee, eat, sleep, repeat"

print(message.startswith("Code")) # output: True
print(message.endswith("repeat")) # output: True
print(message.endswith("back")) # output: false

def web_slice(site: str):
    slice_www = slice(4,-4)
    slice_www_extra = slice(4,-7)
    slice_http = slice(7,-4)
    slice_http_extra = slice(7,-7)
    
    if site.startswith("www"):
        if site.endswith("com"):
            return site[slice_www]
        
        else:
            return site[slice_www_extra]
    
    elif site.startswith("http"):
        if site.endswith("com"):
            return site[slice_http]
        
        else:
            return site[slice_http_extra]

website3 = "www.asshat.com.au"
website4 = "http://aussiemilfs.com"

print(web_slice(website3))
print(web_slice(website4))

# Capitalize every other char

word = input("Enter any word: ")
out = ""

for i in range(len(word)):
    if i % 2 == 1:
        out += word[i].upper()
    else:
        out += word[i]
        
print(out)

