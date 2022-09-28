import random
import tkinter as tk

master = tk.Tk()
# master.iconbitmap("./Tkinter/Phoenix.ico")
sv = tk.StringVar()
sv.set('You are walking around with an open wallet like a dumb ass...')  # ! understood all this
lab = tk.Label(master, textvar=sv)


def user_found_money(event=None):
    amount = event.x  # ! need info on "EVENT" please
    # ? event, here, is the argument you defined for the function. In general, an "event" is something that you trigger,
    # ? or cause, either by having coded it or using built-in Python events (like mouse events or keyboard events)
    # ? .x here shows you added a property to your event argument, like adding a limb to the body of your 'object'
    sv.set('You found $' + str(amount))


def user_lost_money(event=None):
    amount = event.x
    sv.set('You dropped $' + str(amount))


def emit_custom_event():
    choices = ['find', 'lose']  # ! need info on "choices" please or are these arguments
    choice = random.choice(choices)

    # ? choices, here is a list you created with 2 elements to choose from.
    # ? .choice in random is the range or items to choose from that you can define. i.e.:
    # ? mylist = ["apple", "banana", "cherry"]
    # ? print(random.choice(mylist))
    # ? .choice randomly selects one item from the list

    if choice == 'find':
        master.event_generate("<<Find>>",
                              x=random.randint(0, 500))  # ! also random.randint please, I know what random is
        # ? randint is a method that generates only random numbers. In brackets, the arguments are:
        # ? randint(start, stop). I..: print(random.randint(1, 9))

    else:
        master.event_generate("<<Lose>>", x=random.randint(0, 50))

    master.after(6969, emit_custom_event)


lab.pack(padx=75, pady=50)

master.bind("<<Find>>", user_found_money)
master.bind("<<Lose>>", user_lost_money)

master.after(4000, emit_custom_event)

master.mainloop()

# ! please note I just copy and paste but changed a few things to suit me
# ? That's all good. We all do it. Can't code these days if you're not looking stuff up.
