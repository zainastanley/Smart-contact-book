import tkinter as tk

root=tk.Tk()
root.title("Smart Contact Book")
root.geometry("500x500")

def save_contact():
    name=name_entry.get()
    phone=phone_entry.get()

    with open("contacts.txt", "a") as file:
        file.write(f"{name}, {phone}\n")

    print(f"Saving contact: {name} - {phone}")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

name_label=tk.Label(root, text="Contact Name:")
name_label.pack(pady=5)

name_entry=tk.Entry(root, width=30)
name_entry.pack(pady=5)

phone_label=tk.Label(root, text="Phone Number")
phone_label.pack(pady=5)

phone_entry=tk.Entry(root, width=30)
phone_entry.pack(pady=5)

save=tk.Button(root, text="Save", command=save_contact)
save.pack(pady=15)

root.mainloop()