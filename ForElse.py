people = [{'name': 'John', 'age': 25},
          {'name': 'Jane', 'age': 22},
          {'name': 'Peter', 'age': 30},
          {'name': 'Jenifer', 'age': 28}]

name = input('Enter a name: ')

for person in people:
    if person['name'] == name:
        print("{} is in the list".format(name))
        break

else:
    print("{} is not in the list".format(name))
