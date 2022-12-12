import random
import string
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

chars = list(string.ascii_lowercase + string.ascii_uppercase +
             string.digits + "!@#$%&*_-.")
password = []
random.shuffle(chars)

for i in range(0, 8):
    password.append(random.choice(chars))

print("".join(password))


def send():
    especial_chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%&*_-.")
    temp_password = []
    random.shuffle(especial_chars)

    for i in range(0, 12):
        temp_password.append(random.choice(especial_chars))

    print("".join(temp_password))

    messagebox.showinfo(
        title="Login", message="Temporary password {}".format("".join(temp_password)))


master = Tk()
master.config(pady=5, padx=10)

photo = Image.open('./Tkinter/Code.png')
photo_sized = photo.resize((160, 160))
my_photo = ImageTk.PhotoImage(photo_sized)

label = Label(
    master,
    image=my_photo,
    relief=RAISED,
)

entry = Entry(
    master,
    width=40,
    justify=CENTER
)

button = Button(
    master,
    text="REGISTER",
    command=send
)

label.grid(row=0, column=0, columnspan=2, pady=8)
entry.grid(row=1, column=0, pady=8, padx=3)
button.grid(row=1, column=1, pady=8, padx=3)

master.mainloop()
