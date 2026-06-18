import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root=ctk.CTk()
root.title("Smart Contact Book")
root.geometry("380x320")

def save_contact():
    name=name_entry.get()
    phone=phone_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required!")
        return
    if not phone.isdigit() or len(phone)!=10:
        messagebox.showwarning("Invalid Phone", "Phone Number must only contain numbers and should be 10 digits long!")
        return

    with open("contacts.txt", "a") as file:
        file.write(f"{name}, {phone}\n")

    messagebox.showinfo("Success", f"Contact '{name}' saved successfully!")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

title_label=ctk.CTkLabel(root, text="Smart Contact Book", font=("Ariel",20,"bold"))
title_label.pack(pady=15)

name_label=ctk.CTkLabel(root, text="Contact Name:", font=("ariel",12))
name_label.pack(pady=2)

name_entry=ctk.CTkEntry(root, width=250, placeholder_text="Enter name here...")
name_entry.pack(pady=5)

phone_label=ctk.CTkLabel(root, text="Phone Number", font=("Ariel",12))
phone_label.pack(pady=2)

phone_entry=ctk.CTkEntry(root, width=250, placeholder_text="Enter phone number...")
phone_entry.pack(pady=5)

save=ctk.CTkButton(root, text="Save", command=save_contact, corner_radius=8)
save.pack(pady=20)

root.mainloop()