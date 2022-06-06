
#? zip(*iterables) aggregates elements from 2 or more iterables
#?                 creates a zip object with paired elements i tuples for each element

usernames = ["Melca", "Irvin", "Sue"]
passwords = ("passw0rd", "12@3", "swordfish")

users = dict(zip(usernames, passwords)) #zipping the above list whitst casting it into a dictionary

for key,value in users.items():
    print("[user]:{} → [password]:{} ".format(key,value))
    
print()
print("••••••••••••••••••••••••••••••••••")
print()

login_dates = ["01/01/2020", "03/04/2021", "09/24/2021"]

registry = tuple(zip(usernames, passwords, login_dates))

for i in registry:
    print(i)