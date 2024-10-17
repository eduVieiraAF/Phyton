import json

person = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "hasChildren": True,
    "children": ["Alice", "Bob"],
    "pets": None,
    "cars": [
        {"model": "BMW", "year": 2019},
        {"model": "Audi", "year": 2020}
    ]
}

personJson = json.dumps(person, indent=4)
# print(personJson)

with open("./Py_intermediate_concepts/person.json", "w") as f:
    file = json.dumps(person, indent=4)
    # print(file)
    
with open("./Py_intermediate_concepts/crypto.json", "r") as coin:  
    data = json.load(coin)
    # print(data)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable") 
    

user = User("John", 25)
userJson = json.dumps(user, default=encode_user)
print(userJson)