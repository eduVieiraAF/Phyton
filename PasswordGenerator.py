import random
import string

chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%&*_-.")
password = []
random.shuffle(chars)

for i in range(0, 8):
    password.append(random.choice(chars))

print("".join(password))
