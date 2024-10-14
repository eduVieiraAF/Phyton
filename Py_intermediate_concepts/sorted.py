people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 22},
    {'name': 'Peter', 'age': 30},
    {'name': 'Jenifer', 'age': 28},
    {'name': 'Bob', 'age': 35},
    {'name': 'Alice', 'age': 32},
    {'name': 'Charlie', 'age': 27},
    {'name': 'Jenifer', 'age': 58},
]

# key = lambda person: person['age'] # sort by age
sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)

sorted_people = sorted(people, key=lambda person: person['name'], reverse=True)
print(sorted_people)