import random
import string

chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%&*_-.")
password = []

for i in range(0, 12):
    password.append(random.choice(chars))

random.shuffle(chars)

print("".join(password))
