from tkinter import *
from values import *

calc_window = Tk()
calc_window.title("Totalizer")
#calc_window.geometry("330x450")
calc_window.config(padx=8, pady=8, relief="raised", bd=5, background="#132020")
calc_window.iconbitmap("C:\\Users\\edu_v\\Python\\Tkinter\\Calculator\\Images\\calc.ico")

frm_outline = Frame(
    calc_window,
    relief="groove",
    bd=6,
    bg=primary_color,
    padx=10,
    pady=10
)

lbl_display = Label(
    calc_window,
    text="1234567890+-/*=CE",
    bg=primary_dark_variant,
    fg=secondary_light_variant,
    font=(lbl_font, 23,"bold"),
    relief="sunken",
    bd=7,
    padx=10,
    pady=10
    )

button_ce = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text="CE",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
)

button_div = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text="/",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
)

button_times = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text="*",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
)

button_minus = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text="-",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
)

button7 = Button(
    frm_outline,
    bg=primary_dark_variant,
    fg="white",
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    text="7",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
)

button8 = Button(
    frm_outline,
    bg=primary_dark_variant,
    fg="white",
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    text="8",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12
)

button9 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="9",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12
)

button_plus = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text="+",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12
)

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

calc_window.mainloop()