import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import sqlite3

#Application Configuration
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#Database Initialization
conn=sqlite3.connect("contacts.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")
conn.commit()
conn.close()

root=ctk.CTk()
root.title("Smart Contact Book")
root.geometry("680x420")

# Function to switch between frames
def show_frame(frame_to_show):
    welcome_frame.pack_forget()
    add_frame.pack_forget()
    search_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()
    frame_to_show.pack(side="right",fill="both", expand=True, padx=20, pady=20)

# Function to save contact information
def save_contact():
    name=name_entry.get().strip()
    phone=phone_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required!")
        return
    if not phone.isdigit() or len(phone)!=10:
        messagebox.showwarning("Invalid Phone", "Phone Number must only contain numbers and should be 10 digits long!")
        return
    
    #----SQL storage----
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()

    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))

    conn.commit()
    conn.close()
    #-------------------

    messagebox.showinfo("Success", f"Contact '{name}' saved successfully!")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to search for a contact
def search_contact():
    query=search_entry.get().strip()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a name to search!")
        return
    #---SQL Search---
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("SELECT name, phone FROM contacts WHERE LOWER(name)=LOWER(?)", (query,))
    results=cursor.fetchall()
    conn.close()
    #----------------

    if results:
        contact_name=results[0][0]
        contact_phone=results[0][1]
        result_label.configure(text=f"Name: {contact_name}\nPhone: {contact_phone}", text_color="white")
    else:
        result_label.configure(text="Contact not found.", text_color="red")

#Function to update contact
def update_contact():
    target_name=update_name_entry.get().strip()
    new_phone=update_phone_entry.get().strip()

    if not target_name or not new_phone:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return
    if not new_phone.isdigit() or len(new_phone)!=10:
        messagebox.showwarning("Invalid Phone", "Phone Number must only contain numbers and should be 10 digits long!")
        return
    
    #---SQL Update---
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE contacts SET phone=? WHERE LOWER(name)=LOWER(?)", (new_phone, target_name))
    rows_affected=cursor.rowcount
    conn.commit()
    conn.close()
    #----------------

    if rows_affected>0:
        messagebox.showinfo("Success", f"Contact '{target_name}' updated successfully!")
        update_name_entry.delete(0, tk.END)
        update_phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Not Found", f"Contact '{target_name}' not found!")

#Function to delete contact
def delete_contact():
    target_name=delete_entry.get().strip()

    if not target_name:
        messagebox.showwarning("Input Error", "Please enter a name to delete!")
        return
    
    confirm=messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete contact '{target_name}'?")
    if not confirm:
        return
    
    #---SQL Delete---
    conn=sqlite3.connect("contacts.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE LOWER(name)=LOWER(?)", (target_name,))
    rows_affected=cursor.rowcount
    conn.commit()
    conn.close()
    #----------------

    if rows_affected>0:
        messagebox.showinfo("Success", f"Contact '{target_name}' deleted successfully!")
        delete_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Not Found", f"Contact '{target_name}' not found!")

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

btn_update=ctk.CTkButton(sidebar, text="Update Contact", command=lambda: show_frame(update_frame))
btn_update.pack(pady=10, padx=10)

btn_delete=ctk.CTkButton(sidebar, text="Delete Contact", command=lambda: show_frame(delete_frame))
btn_delete.pack(pady=10, padx=10)

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

# Update Contact Frame
update_frame=ctk.CTkFrame(root, fg_color="transparent")

update_title=ctk.CTkLabel(update_frame, text="Update Contact", font=("Arial",20,"bold"))
update_title.pack(pady=15)

update_name_label=ctk.CTkLabel(update_frame, text="Contact Name to Update:", font=("Arial",12))
update_name_label.pack(pady=2)

update_name_entry=ctk.CTkEntry(update_frame, width=250, placeholder_text="Enter name of contact to update...")
update_name_entry.pack(pady=5)

update_phone_label=ctk.CTkLabel(update_frame, text="New Phone Number:", font=("Arial",12))
update_phone_label.pack(pady=2)

update_phone_entry=ctk.CTkEntry(update_frame, width=250, placeholder_text="Enter new phone number...")
update_phone_entry.pack(pady=5)

update_button=ctk.CTkButton(update_frame, text="Update Info", command=update_contact)
update_button.pack(pady=20)

# Delete Contact Frame
delete_frame=ctk.CTkFrame(root, fg_color="transparent")

delete_title=ctk.CTkLabel(delete_frame, text="Delete Contact", font=("Arial",20,"bold"))
delete_title.pack(pady=15)

delete_name_label=ctk.CTkLabel(delete_frame, text="Contact Name to Delete:", font=("Arial",12))
delete_name_label.pack(pady=2)

delete_entry=ctk.CTkEntry(delete_frame, width=250, placeholder_text="Enter name of contact to delete...")
delete_entry.pack(pady=5)

delete_button=ctk.CTkButton(delete_frame, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=20)

# Initial Frame Display
show_frame(welcome_frame)

root.mainloop()