import tkinter as tk

root=tk.Tk()
root.title("Smart Contact Book")
root.geometry("500x500")

name_label=tk.Label(root, text="Contact Name:")
name_label.pack(pady=5)

name_entry=tk.Entry(root, width=30)
name_entry.pack(pady=5)

phone_label=tk.Label(root, text="Phone Number")
phone_label.pack(pady=5)

phone_entry=tk.Entry(root, width=30)
phone_entry.pack(pady=5)

save_button=tk.Button(root, text="Save")
save_button.pack(pady=15)

root.mainloop()