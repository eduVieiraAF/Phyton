from tkinter import *
from tkinter import messagebox
from values import *

expression = ""

def press(num):
    global expression
    
    expression = expression + str(num)
    equation.set(expression)
    
def clear():
    global expression
    expression = ""
    equation.set("")
    
def equal_press():
    global expression
    
    try:
        total = str(eval(expression))
        equation.set(total)
        expression=total
    
    except:
        equation.set("ERROR")
        expression = ""
    
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def invert():
    global expression
    expression = "-" + expression
    expression = str(eval(expression))
    equation.set(expression)
       

calc_window = Tk()
calc_window.title("Totalizer")
calc_window.resizable(False, False)
calc_window.config(padx=12, pady=12, relief="raised", bd=3, background=primary_light_variant)
calc_window.iconbitmap("C:\\Users\\edu_v\\Python\\Tkinter\\Calculator\\Images\\calc.ico")

equation = StringVar()
    
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
    textvariable=equation,
    bg=primary_dark_variant,
    fg=secondary_light_variant,
    font=(lbl_font, 23,"bold"),
    relief="sunken",
    bd=7,
    width=15,
    padx=10,
    pady=10,
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
    command=clear
)

button_backsapce = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text="←",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=backspace
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
    command=lambda: press("/")
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
    command=lambda: press("*")
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
    command=lambda: press("7")
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
    pady=12,
    command=lambda: press("8")
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
    pady=12,
    command=lambda: press("9")
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
    command=lambda: press("-")
)

button4 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="4",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("4")
)

button5 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="5",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("5")
)

button6 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="6",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("6")
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
    pady=12,
    command=lambda: press("+")
)

button1= Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="1",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("1")
)

button2 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="2",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("2")
)

button3 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="3",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("3")
)

button_dot = Button(
    frm_outline,
    bg=secondary_light_variant,
    activebackground=secondary_dark_variant,
    activeforeground=primary_light_variant,
    fg=primary_dark_variant,
    text=".",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press(".")
)

button_plus_minus = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="+/-",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=invert
)

button0 = Button(
    frm_outline,
    bg=primary_dark_variant,
    activebackground=primary_light_variant,
    activeforeground=primary_dark_variant,
    fg="white",
    text="0",
    font=(btn_font, 16, "bold"),
    height=btn_height,
    width=btn_width,
    padx=12,
    pady=12,
    command=lambda: press("0")
)

button_equals = Button(
    frm_outline,
    bg=secondary_inverted,
    activebackground=secondary_inverted_dark,
    activeforeground=secondary_inverted_light,
    fg="white",
    text=" = ",
    font=(btn_font, 16, "bold"),
    width=8,
    padx=15,
    pady=12,
    bd=2,
    command=equal_press
)


lbl_display.pack(side=TOP)
frm_outline.pack(side=BOTTOM)

button_ce.grid(row=0,column=0)
button_backsapce.grid(row=0,column=1)
button_div.grid(row=0,column=2)
button_times.grid(row=0,column=3)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_minus.grid(row=1,column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_plus.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_dot.grid(row=3, column=3)

button_plus_minus.grid(row=4, column=0)
button0.grid(row=4, column=1)
button_equals.grid(row=4, column=2, columnspan=2)


calc_window.mainloop()
