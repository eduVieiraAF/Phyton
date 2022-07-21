from tkinter import *

#* VALUES
primary_color = "#455a64"
primary_light_variant = "#718792"
primary_dark_variant = "#1c313a"

secondary_color = "#00838f"
secondary_light_variant = "#4fb3bf"
secondary_dark_variant = "#005662"

btn_font = "Bookman"
lbl_font = "Lato"

#•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••


calc_window = Tk()
# calc_window.geometry("460x460")
calc_window.title("Totalizer")
calc_window.iconbitmap("./Tkinter/calc.ico")

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
    font=(lbl_font, 17,"bold"),
    relief="sunken",
    bd=12,
    padx=10,
    pady=10
    )

button7 = Button(
    frm_outline,
    bg=primary_dark_variant,
    fg="white",
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    text="7",
    font=(btn_font, 16, "bold"),
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
    padx=12,
    pady=12
)

lbl_display.pack(side=TOP)
frm_outline.pack(side=BOTTOM)
button7.grid(row=0,column=0)
button8.grid(row=0,column=1)
button9.grid(row=0,column=2)
button_plus.grid(row=0,column=3)

calc_window.mainloop()