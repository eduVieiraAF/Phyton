from tkinter import *
from values import *
from Calculator import *

calc_window = Tk()
calc_window.title("Totalizer")
calc_window.resizable(False, False)
calc_window.config(padx=12, pady=12, relief="raised", bd=5, background=primary_light_variant)
calc_window.iconbitmap("C:\\Users\\edu_v\\Python\\Tkinter\\Calculator\\Images\\calc.ico")

lbl_display.pack(side=TOP)
frm_outline.pack(side=BOTTOM)

button_ce.grid(row=0,column=0)
button_div.grid(row=0,column=1)
button_times.grid(row=0,column=2)
button_minus.grid(row=0,column=3)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_plus.grid(row=1,column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_dot.grid(row=2, column=3)


calc_window.mainloop()