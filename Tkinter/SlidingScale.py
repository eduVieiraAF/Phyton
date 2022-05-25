from statistics import geometric_mean
from tkinter import *
from turtle import left

def submit():
    print("The temperature is currently {}º C.". format(scale.get()))

window = Tk()
window.geometry("500x500")
window.title("Python coding by Edu")
window.iconbitmap('./Tkinter/python.ico')

hot_image = PhotoImage(file='./Tkinter/fire.png')
hot_label = Label(image = hot_image)
hot_label.pack()

scale = Scale(
    window,
    from_="100", 
    to="-30",
    length=400,
    orient=VERTICAL,
    font=("Consolas", 13),
    tickinterval=20,
    troughcolor="#8bb9dd",
    fg="#31639c",
    bg="#d9e6ee" 
    )
#scale.set(25)
scale.set(((scale["from"] - scale["to"])/2) + scale["to"]) # places indicator in the middle
scale.pack()

button = Button(
    window, 
    text="Submit", 
    font=("Arial", 16), 
    command=submit
    )

cold_image = PhotoImage(file='./Tkinter/snow.png')
cold_label = Label(image = cold_image)
cold_label.pack()

button.pack()

window.mainloop()