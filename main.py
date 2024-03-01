import tkinter as tk
from tkinter import messagebox
from datetime import date

def get_user_birthday():
    birth_year = int(entry_year.get())
    birth_month = int(entry_month.get())
    birth_day = int(entry_day.get())

    user_birthday = date(birth_year, birth_month, birth_day)

    return user_birthday

def calculate_age():
    try:
        user_birthday = get_user_birthday()
        today = date.today()
        year_diff = today.year - user_birthday.year
        precedes_flag = ((today.month, today.day) < (user_birthday.month, user_birthday.day))
        age = year_diff - precedes_flag
        messagebox.showinfo("Age", f"Your age is: {age}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid birth date.")

root = tk.Tk()
root.title("Age Calculator")

label_year = tk.Label(root, text="Enter your birth year:")
label_year.grid(row=0, column=0, padx=10, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=0, column=1, padx=10, pady=5)

label_month = tk.Label(root, text="Enter your birth month:")
label_month.grid(row=1, column=0, padx=10, pady=5)
entry_month = tk.Entry(root)
entry_month.grid(row=1, column=1, padx=10, pady=5)

label_day = tk.Label(root, text="Enter your birth day:")
label_day.grid(row=2, column=0, padx=10, pady=5)
entry_day = tk.Entry(root)
entry_day.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
