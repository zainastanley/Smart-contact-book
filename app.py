import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

#Application Configuration
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root=ctk.CTk()
root.title("Smart Contact Book")
root.geometry("680x420")

# Function to switch between frames
def show_frame(frame_to_show):
    welcome_frame.pack_forget()
    add_frame.pack_forget()
    search_frame.pack_forget()
    frame_to_show.pack(side="right",fill="both", expand=True, padx=20, pady=20)

# Function to save contact information
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

# Function to search for a contact
def search_contact():
    query=search_entry.get().strip().lower()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a name to search!")
        return
    try:
        with open("contacts.txt", "r") as file:
            lines=file.readlines()
    except FileNotFoundError:
        messagebox.showinfo("Error", "No contacts found.")
        return
    for line in lines:
        parts=line.strip().split(", ")
        if len(parts)==2:
            contact_name=parts[0]
            contact_phone=parts[1]
            if contact_name.lower()==query:
                result_label.configure(text=f"Name: {contact_name}\nPhone: {contact_phone}", text_color="white")
                return
    result_label.configure(text="Contact not found.", text_color="red")

# Sidebar Menu
sidebar=ctk.CTkFrame(root, width=150, corner_radius=0)
sidebar.pack(side="left", fill="y")

logo_label=ctk.CTkLabel(sidebar, text="Contact Menu", font=("Ariel",16,"bold"))
logo_label.pack(pady=10, padx=10)

btn_home=ctk.CTkButton(sidebar, text="Home", command=lambda: show_frame(welcome_frame))
btn_home.pack(pady=10, padx=10)

btn_add=ctk.CTkButton(sidebar, text="Add Contact", command=lambda: show_frame(add_frame))
btn_add.pack(pady=10, padx=10)

btn_search=ctk.CTkButton(sidebar, text="Search Contact", command=lambda: show_frame(search_frame))
btn_search.pack(pady=10, padx=10)

#Welcome Frame
welcome_frame=ctk.CTkFrame(root, fg_color="transparent")

welcome_title=ctk.CTkLabel(welcome_frame, text="Welcome to Smart Contact Book!", font=("Ariel",22,"bold"))
welcome_title.pack(pady=(120,10))

welcome_subtitle=ctk.CTkLabel(welcome_frame, text="Select an option from the menu to begin.", font=("Ariel",14), text_color="gray")
welcome_subtitle.pack(pady=10)

# Add Contact Frame
add_frame=ctk.CTkFrame(root, fg_color="transparent")
                   
title_label=ctk.CTkLabel(add_frame, text="Smart Contact Book", font=("Arial",20,"bold"))
title_label.pack(pady=15)

name_label=ctk.CTkLabel(add_frame, text="Contact Name:", font=("Arial",12))
name_label.pack(pady=2)

name_entry=ctk.CTkEntry(add_frame, width=250, placeholder_text="Enter name here...")
name_entry.pack(pady=5)

phone_label=ctk.CTkLabel(add_frame, text="Phone Number", font=("Arial",12))
phone_label.pack(pady=2)

phone_entry=ctk.CTkEntry(add_frame, width=250, placeholder_text="Enter phone number...")
phone_entry.pack(pady=5)

save=ctk.CTkButton(add_frame, text="Save", command=save_contact, corner_radius=8)
save.pack(pady=20)

# Search Contact Frame
search_frame=ctk.CTkFrame(root, fg_color="transparent")

search_title=ctk.CTkLabel(search_frame, text="Search Contact", font=("Arial",20,"bold"))
search_title.pack(pady=15)

search_entry=ctk.CTkEntry(search_frame, width=250, placeholder_text="Enter contact to search...")
search_entry.pack(pady=10)

search_button=ctk.CTkButton(search_frame, text="Search", command=search_contact)
search_button.pack(pady=10)

result_label=ctk.CTkLabel(search_frame, text="", font=("Arial",14,"bold"))
result_label.pack(pady=20)

# Initial Frame Display
show_frame(welcome_frame)

root.mainloop()