import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def save_qr_code():
    data = entry.get()
    if data:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if filename:
            generate_qr_code(data, filename)
            messagebox.showinfo("Info", "QR Code saved successfully!")
    else:
        messagebox.showerror("Error", "Enter data to generate QR code")

def show_qr_code():
    data = entry.get()
    if data:
        filename = "temp_qrcode.png"
        generate_qr_code(data, filename)
        img = Image.open(filename)
        img = img.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        qr_label.config(image=img)
        qr_label.image = img
    else:
        messagebox.showerror("Error", "Enter data to generate QR code")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x650")

label = tk.Label(
    root, 
    text="Enter data:",
    font=("Arial", 18))


entry = tk.Entry(root)


save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)


show_button = tk.Button(root, text="Show QR Code", command=show_qr_code)


qr_label = tk.Label(root)


label.pack()
entry.pack(pady=8)
save_button.pack(pady=4)
show_button.pack(pady=4)
qr_label.pack(pady=8)

root.mainloop()
