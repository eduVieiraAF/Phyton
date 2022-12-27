from io import BytesIO
from tkinter import *
from tkinter import messagebox

import requests
from PIL import Image, ImageTk

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
url_photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXO5BhkdXL6dxDn2DG1SZg4ZCI6kFwj5bIIg&usqp=CAU"

response = requests.get(url)
get_image = requests.get(url_photo)

if response.status_code == 200:
    data = response.json()
    coin = data["chartName"]
    currency = data["bpi"]["USD"]["code"]
    price = data["bpi"]["USD"]["rate"]
    lastestRate = data["time"]["updated"]
    # print(price)
    print(f"The current price of {coin} at {lastestRate} is {currency} ${price}")
    print(data["disclaimer"])
    # print(lastestRate)

else:
    messagebox.showerror(title="ERROR", message=str(response.status_code))
    print(response.status_code)

master = Tk()
master.title("Bitcoin price")
master.resizable(False, False)
master.config(padx=5, pady=5)

image = Image.open(BytesIO(get_image.content))
photo = ImageTk.PhotoImage(image)

Label(master, image=photo, relief=GROOVE, text=lastestRate, compound=TOP).pack()

frame = Frame(master, padx=5, pady=5, relief="groove")

lbl_currency = Label(frame, padx=5, pady=5, font=("Arial", 18), text=currency)
lbl_price = Label(frame, padx=5, pady=5, font=("Arial", 18), text=price)

frame.pack()
lbl_currency.grid(row=0, column=0)
lbl_price.grid(row=0, column=1)

master.mainloop()
