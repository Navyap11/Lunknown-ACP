import tkinter as tk
from datetime import date

def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()

    age = today.year - year

    if (today.month, today.day) < (month, day):
        age = age - 1

    result_label.config(text="Your Age is: " + str(age) + " years")

window = tk.Tk()
window.title("Age Calculator")
window.geometry("400x300")

tk.Label(window, text="Enter Date of Birth").pack(pady=10)

tk.Label(window, text="Day").pack()
day_entry = tk.Entry(window)
day_entry.pack()

tk.Label(window, text="Month").pack()
month_entry = tk.Entry(window)
month_entry.pack()

tk.Label(window, text="Year").pack()
year_entry = tk.Entry(window)
year_entry.pack()

tk.Button(window, text="Calculate Age", command=calculate_age).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()