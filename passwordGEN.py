import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_copy_password():
    password_length = int(length_entry.get())
    generated_password = generate_password(password_length)
    result_label.config(text=f'Generated Password: {generated_password}')

    # Copy password to clipboard
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()

# Create the graphical interface
root = tk.Tk()
root.title("Password Generator")

# Interface elements
length_label = ttk.Label(root, text="Password Length:")
length_entry = ttk.Entry(root)
generate_button = ttk.Button(root, text="Generate Password and Copy", command=generate_and_copy_password)
result_label = ttk.Label(root, text="Generated Password: ")

# Element layout
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Starts the graphical interface loop
root.mainloop()
