import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a SQLite database to store information
conn = sqlite3.connect("homeless_elderly.db")
c = conn.cursor()

# Create a table to store individual information
c.execute('''CREATE TABLE IF NOT EXISTS elderly_individuals
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              age INTEGER,
              contact_number TEXT,
              needs TEXT)''')
conn.commit()

# Function to add an elderly individual to the database
def add_individual():
    name = name_entry.get()
    age = age_entry.get()
    contact_number = contact_entry.get()
    needs = needs_entry.get("1.0", tk.END)

    if name and age and contact_number and needs:
        c.execute("INSERT INTO elderly_individuals (name, age, contact_number, needs) VALUES (?, ?, ?, ?)",
                  (name, age, contact_number, needs))
        conn.commit()
        messagebox.showinfo("Success", "Elderly individual added to the database.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    needs_entry.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Assisting Homeless Elderly Interface")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

contact_label = tk.Label(root, text="Contact Number:")
contact_label.pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

needs_label = tk.Label(root, text="Needs:")
needs_label.pack()
needs_entry = tk.Text(root, height=5, width=40)
needs_entry.pack()

# Create buttons
add_button = tk.Button(root, text="Add Individual", command=add_individual)
add_button.pack()

clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.pack()

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the application exits
conn.close()