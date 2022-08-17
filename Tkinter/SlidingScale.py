from tkinter import *


def submit():
    if scale.get() < 0:
        print("Freezing... Got a radiator?")

    if scale.get() > 35:
        print("Turn on the AC...")

    print("The temperature is currently {}º C.".format(scale.get()))


window = Tk()
window.geometry("500x500")
window.title("Python coding by Edu")

hot_image = PhotoImage(file='fire.png')
hot_label = Label(image=hot_image)
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
# scale.set(25)
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])  # places indicator in the middle
scale.pack()

button = Button(
    window,
    text="Submit",
    font=("Arial", 16),
    command=submit
)

cold_image = PhotoImage(file='snow.png')
cold_label = Label(image=cold_image)
cold_label.pack()

button.pack()

window.mainloop()
