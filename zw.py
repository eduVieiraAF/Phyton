# Open and reading a file

file = open("test.txt", "r")

print(file.read())

file.close()

# * with open will automatically close file

try:
    with open('test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
    
# * it is good practice to sound the code with try and except


# * copyfile() = copies the content of a file

import shutil

shutil.copyfile('test.txt', 'text_copy.txt') # source, destination/create file's name


#label is an area widget that holds text and/or image

import tkinter as tk

window1 = tk.Tk()
window1.title('Window 1 → centered')

window_width = 460
window_height = 460

# get the screen dimension
screen_width = window1.winfo_screenwidth()
screen_height = window1.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window1.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

window1.mainloop()

window2 = tk.Tk()

window2.title('Window 2 → sized manually and not resizable')
window2.geometry('1000x400+50+50') # windown.geometry('width x height ± x ± y)
window2.resizable(False, False)

window2.mainloop()

# Transparency

window3 = tk.Tk()

window3.title('Window 3 → transparent')
window3.geometry('600x400')
window3.attributes('-alpha', 0.7)

window3.mainloop()

window4 = tk.Tk()

window4.title('Window 4 - with personalized icon')
window4.geometry('1000x400')
window4.resizable(False, True)
window4.iconbitmap('./Tkinter/Phoenix.ico')

window4.mainloop()


from tkinter import *

window = Tk()
window.title("Labels")
window.iconbitmap('./Tkinter/python.ico')

photo = PhotoImage(file='./Tkinter/spaceship.png')

label = Label(
    window, 
    text="hello, Earth dwellers!", 
    font=("Arial", 40,"bold"), 
    fg="#562f7e",
    bg="#e7eef5",
    relief=SUNKEN, #border
    bd=5, #border width
    padx=20,
    pady=20,
    image=photo,
    compound="top"
    )
#label.place(x=0,y=0) places whereever i choose
label.pack()


window.mainloop()