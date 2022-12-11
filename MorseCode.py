from tkinter import *
from tkinter import messagebox

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}


def encrypt(message):
    cipher = ""

    for letter in message:
        if letter != " ":
            cipher += morse_code_dict[letter] + " "

        else:
            cipher += " "

    return cipher


def send():
    string = entry.get()
    code = encrypt(str(string.upper()))
    messagebox.showinfo(title="Encryption", message=code)
    entry.delete(0, END)


window = Tk()
window.title("Phoenix code")
window.resizable(False, False)
window.config(padx=10, pady=10)

# string =StringVar()

entry = Entry(
    window,
    width=45,
    font=("Arial", 23),
    foreground="#82c59c",
    background="#3d3d3e",
    borderwidth=3,
    justify=CENTER,
)

send_btn = Button(
    window,
    text="SUBMIT",
    command=send)

entry.pack(side=LEFT, padx=4)
send_btn.pack(side=RIGHT, padx=4)

window.mainloop()
