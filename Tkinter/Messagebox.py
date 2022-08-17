from tkinter import Tk, messagebox, Button

window = Tk()
window.title("Python coding by Edu")
window.geometry("350x150")


def click():
    times = 3
    messagebox.showinfo(title="Nope", message="Nothing happens when ya click.")
    messagebox.showwarning(title="DANGER", message="Does it though???")
    while times > 0:
        messagebox.showerror(title="Something's off",
                             message="Something went wrong and your PC is not running properly.")
        times -= 1

    if messagebox.askokcancel(title="Continue?", message="Your computer is not well and needs to be rebooted."):
        messagebox.showerror("Oh well", message="Something is still not right.")

    else:
        messagebox.showwarning(title="Hmm...", message="You will regret it later.")

    if messagebox.askretrycancel(title="Go again?",
                                 message="Your computer is not well and still needs to be rebooted. Try again?"):
        messagebox.showinfo("How about that?", message="Ain't gonna be rebooted but bug has been fixed.")

    else:
        messagebox.showinfo("How about that?", message="Seems like bug went away.")

    if messagebox.askyesno(title="Proceed", message="Do you want to continue?"):
        messagebox.showinfo("Python", message="Keep coding...")

    else:
        if messagebox.askyesno("You sure?", message="Last change. Go back?"):
            messagebox.showinfo("Alright!", message="Coding thru the night!")

        else:
            messagebox.showinfo("Bye", message="See ya next time.")
            answer = messagebox.askquestion(title="REALLY!?", message="Come on, let's keep going.")
            if answer == "yes":
                messagebox.showinfo("Alright!", message="Coding thru the night!")
                options = messagebox.askyesnocancel(title="Python?", message="So let's go with Python?")
                if options:
                    messagebox.showinfo("Alright!", message="Python it is.")
                
                if not options:
                    messagebox.showerror("NO!", message="We're NOT coding in Kotlin tonight!")

                else:
                    messagebox.showinfo("F«»k!", message="Get atta here!")

            else:
                messagebox.showwarning("Pussy", message="You're WEAK!")


button = Button(
    window,
    command=click,
    text="Click me",
    font=("Arial", 22),
    bg="#188bc2",
    activebackground="#4a5176",
    fg="White",
    activeforeground="White"
)

button.pack()

window.mainloop()
