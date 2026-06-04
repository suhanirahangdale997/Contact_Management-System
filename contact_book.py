import tkinter as tk
from tkinter import messagebox

contacts = []

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    messagebox.showinfo("Success", "Contact Added Successfully")
    clear_fields()
    display_contacts()

# Display Contacts
def display_contacts():
    listbox.delete(0, tk.END)

    for contact in contacts:
        listbox.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']}"
        )

# Search Contact
def search_contact():
    keyword = search_entry.get().lower()

    listbox.delete(0, tk.END)

    found = False

    for contact in contacts:
        if (keyword in contact["name"].lower() or
                keyword in contact["phone"]):

            listbox.insert(
                tk.END,
                f"{contact['name']} - {contact['phone']}"
            )
            found = True

    if not found:
        messagebox.showinfo("Search", "No Contact Found")

# Load Selected Contact
def select_contact(event):
    try:
        index = listbox.curselection()[0]
        selected = contacts[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected["name"])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, selected["phone"])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, selected["email"])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, selected["address"])

    except:
        pass

# Update Contact
def update_contact():
    try:
        index = listbox.curselection()[0]

        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }

        messagebox.showinfo("Success", "Contact Updated")
        display_contacts()
        clear_fields()

    except:
        messagebox.showerror(
            "Error",
            "Please Select a Contact"
        )

# Delete Contact
def delete_contact():
    try:
        index = listbox.curselection()[0]

        del contacts[index]

        messagebox.showinfo(
            "Success",
            "Contact Deleted"
        )

        display_contacts()
        clear_fields()

    except:
        messagebox.showerror(
            "Error",
            "Please Select a Contact"
        )

# Clear Fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("700x500")
root.config(bg="lightblue")

# Labels and Entries
tk.Label(root, text="Name", bg="lightblue",
         font=("Arial", 12)).place(x=30, y=20)

name_entry = tk.Entry(root, width=40)
name_entry.place(x=150, y=20)

tk.Label(root, text="Phone", bg="lightblue",
         font=("Arial", 12)).place(x=30, y=60)

phone_entry = tk.Entry(root, width=40)
phone_entry.place(x=150, y=60)

tk.Label(root, text="Email", bg="lightblue",
         font=("Arial", 12)).place(x=30, y=100)

email_entry = tk.Entry(root, width=40)
email_entry.place(x=150, y=100)

tk.Label(root, text="Address", bg="lightblue",
         font=("Arial", 12)).place(x=30, y=140)

address_entry = tk.Entry(root, width=40)
address_entry.place(x=150, y=140)

# Buttons
tk.Button(root, text="Add Contact",
          command=add_contact,
          bg="green",
          fg="white").place(x=50, y=200)

tk.Button(root, text="Update Contact",
          command=update_contact,
          bg="orange").place(x=170, y=200)

tk.Button(root, text="Delete Contact",
          command=delete_contact,
          bg="red",
          fg="white").place(x=310, y=200)

# Search
tk.Label(root, text="Search",
         bg="lightblue",
         font=("Arial", 12)).place(x=30, y=260)

search_entry = tk.Entry(root, width=30)
search_entry.place(x=150, y=260)

tk.Button(root, text="Search",
          command=search_contact,
          bg="blue",
          fg="white").place(x=400, y=255)

# Contact List
listbox = tk.Listbox(root, width=60, height=10)
listbox.place(x=50, y=320)

listbox.bind("<<ListboxSelect>>", select_contact)

root.mainloop()