import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root=ctk.CTk()
root.title("Smart Contact Book")
root.geometry("380x320")

def save_contact():
    name=name_entry.get()
    phone=phone_entry.get()

    with open("contacts.txt", "a") as file:
        file.write(f"{name}, {phone}\n")

    print(f"Saving contact: {name} - {phone}")

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