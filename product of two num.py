import tkinter as tk

def multiply():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    product = num1 * num2
    result_label.config(text="Product = " + str(product))

window = tk.Tk()
window.title("Multiply Two Numbers")
window.geometry("400x200")

tk.Label(window, text="Enter First Number").pack()
num1_entry = tk.Entry(window)
num1_entry.pack()

tk.Label(window, text="Enter Second Number").pack()
num2_entry = tk.Entry(window)
num2_entry.pack()

tk.Button(window, text="Multiply", command=multiply).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()