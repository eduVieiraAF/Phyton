# label is an area widget that holds text and/or image

from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Labels")

photo = Image.open('/home/eduvieira/IdeaProjects/Python/Tkinter/spaceship.png')
photo_sized = photo.resize((160, 160))
my_photo=ImageTk.PhotoImage(photo_sized)


label = Label(
    window,
    text="hello, Earth dwellers!",
    font=("Arial", 40, "bold"),
    fg="#562f7e",
    bg="#e7eef5",
    relief=SUNKEN,  # border
    bd=5,  # border width
    padx=20,
    pady=20,
    image=my_photo,
    compound="top",
    
)
# label.place(x=0,y=0) places wherever i choose
label.pack()

window.mainloop()
