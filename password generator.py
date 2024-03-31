import tkinter as tk
from tkinter import ttk
import pyperclip
import string
import random

letras = string.ascii_letters
numberss = string.digits
characterss = string.punctuation


def update_spinbox_value(event):
    value = round(scale_var.get())
    spinbox_var.set(value)


def update_scale_value():
    value: str = spinbox_var.get()
    scale_var.set(value)


def copy_to_clipboard():
    text_to_copy = longPass.get()
    if text_to_copy:
        pyperclip.copy(text_to_copy)


def insert_password(password):
    if longPass.get() == '':
        longPass.configure(state="normal")
        longPass.insert(tk.END, password)
        longPass.configure(state="readonly")
    elif longPass.get() != '':
        longPass.configure(state="normal")
        longPass.delete(0, 50)
        longPass.insert(tk.END, password)
        longPass.configure(state="readonly")


def generate_password():
    characters_value = characters.get()
    numbers_value = numbers.get()
    symbols_value = symbols.get()
    charsets = []
    if characters_value:
        charsets.append(string.ascii_letters)
    if numbers_value:
        charsets.append(string.digits)
    if symbols_value:
        charsets.append(string.punctuation)

    if not charsets:
        return  # No hay ningún conjunto de caracteres seleccionado
    password_length = round(scale.get())
    password = ''.join(random.choice(''.join(charsets)) for _ in range(password_length))

    insert_password(password)
    print(password)


root = tk.Tk()
root.config(width=300, height=200)
root.title("Generator password")

# Text
ttk.Label(root, text='Password´s length: ').grid(pady=5, row=0, column=0)
ttk.Label(root, text='Including').grid(pady=5, row=1, column=1)
ttk.Label(root, text='Characters: ').grid(pady=5, row=2, column=0)
ttk.Label(root, text='Numbers: ').grid(pady=5, row=3, column=0)
ttk.Label(root, text='Symbols: ').grid(pady=5, row=4, column=0)



# State Initial Checkbutton
characters = tk.BooleanVar()
numbers = tk.BooleanVar()
symbols = tk.BooleanVar()

characters.set(False)
numbers.set(False)
symbols.set(False)

# Checkbutton
ttk.Checkbutton(root, variable=characters).grid(pady=5, row=2, column=1)
ttk.Checkbutton(root, variable=numbers).grid(pady=5, row=3, column=1)
ttk.Checkbutton(root, variable=symbols).grid(pady=5, row=4, column=1)

# Variable para el Spinbox y el Scale
spinbox_var = tk.StringVar()
scale_var = tk.DoubleVar()

# Spinbox
spinbox = ttk.Spinbox(root, from_=1, to=50, increment=1, textvariable=spinbox_var, command=update_scale_value,
                      state='readonly', width=5)
spinbox.grid(row=0, column=2, padx=10, pady=10)

# Scale (Slider)
scale = ttk.Scale(root, from_=1, to=50, variable=scale_var, command=update_spinbox_value)
scale.grid(row=0, column=1, padx=10, pady=10)

# Entry password
longPass = ttk.Entry(root, width=30, validate='key', state="readonly")
longPass.grid(pady=5, padx=10, row=6, column=0)

# Buttons
ttk.Button(root, text="Generate", command=generate_password).grid(pady=5, row=5, column=1)
ttk.Button(root, text="Copy", command=copy_to_clipboard).grid(pady=5, row=6, column=1)

root.mainloop()
