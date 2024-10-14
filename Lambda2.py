people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 22},
    {'name': 'Peter', 'age': 30},
    {'name': 'Jenifer', 'age': 28},
    {'name': 'Bob', 'age': 35},
    {'name': 'Alice', 'age': 32},
    {'name': 'Charlie', 'age': 27},
]

people.sort(key=lambda person: person['age'])

for person in people:
    print(f"{person['name']} is {person['age']} years old")
    

def call(func):
    func()

def add(a, b):
    return a + b

call(lambda: add(1, 2))