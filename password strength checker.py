import tkinter as tk

def check_password():
    password = password_entry.get()

    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in symbols:
            has_symbol = True

    missing = []

    if len(password) < 8:
        missing.append("at least 8 characters")
    if has_upper==False:
        missing.append("an uppercase letter")
    if has_lower==False:
        missing.append("a lowercase letter")
    if has_number==False:
        missing.append("a number")
    if has_symbol==False:
        missing.append("a symbol")

    if len(missing) == 0:
        result_label.config(text="This password is strong.", fg="green")
    else:
        result_label.config(
            text="Weak password. Missing: " + ", ".join(missing),
            fg="red"
        )

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x250")

title_label = tk.Label(window, text="Enter a Password")
title_label.pack(pady=10)

password_entry = tk.Entry(window, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(window, text="Check Password", command=check_password)
check_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()