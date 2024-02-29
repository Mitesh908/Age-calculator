import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("400x200")

        self.date_label = ttk.Label(self.root, text="Enter your date of birth (YYYY-MM-DD):")
        self.date_label.pack(pady=5)

        self.date_entry = ttk.Entry(self.root)
        self.date_entry.pack(pady=5)

        self.calculate_button = ttk.Button(self.root, text="Calculate Age", command=self.calculate_age)
        self.calculate_button.pack(pady=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=5)

    def calculate_age(self):
        dob_str = self.date_entry.get()
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            current_date = datetime.now()
            age = current_date - dob
            years = age.days // 365
            remaining_days = age.days % 365
            months = remaining_days // 30
            remaining_days = remaining_days % 30
            days = remaining_days
            hours = age.seconds // 3600
            remaining_seconds = age.seconds % 3600
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60

            age_str = f"Age: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds."
            self.result_label.config(text=age_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date in YYYY-MM-DD format.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculatorApp(root)
    root.mainloop()
