import requests
from tkinter import *
from tkinter import messagebox

url = "https://favqs.com/api/qotd"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    tags = data["quote"]["tags"]
    quote = data["quote"]["body"]
    author = data["quote"]["author"]

    print(f'"{quote}"\n\t- {author}\nTags{tags}')

else:
    print(f"ERROR → {response.status_code}")

window = Tk()
window.title("INSPIRATIONAL QUOTE")
window.iconbitmap("./Tkinter/python.ico")
window.resizable(False, False)


window.mainloop()