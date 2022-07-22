from tkinter import *
from values import *
from Main import calc_window

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
    text="0",
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
    pady=12
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
    pady=12
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
    pady=12
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
    pady=12
)


