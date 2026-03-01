import tkinter as tk

def convert():
    value = float(value_entry.get())

    from_unit = from_var.get()
    to_unit = to_var.get()

    if from_unit == "Inches":
        meters = value * 0.0254
    elif from_unit == "Centimeters":
        meters = value / 100
    elif from_unit == "Meters":
        meters = value
    elif from_unit == "Kilometers":
        meters = value * 1000

    if to_unit == "Inches":
        result = meters / 0.0254
    elif to_unit == "Centimeters":
        result = meters * 100
    elif to_unit == "Meters":
        result = meters
    elif to_unit == "Kilometers":
        result = meters / 1000

    result_label.config(text="Result = " + str(round(result, 2)))

window = tk.Tk()
window.title("Length Converter")
window.geometry("400x300")

tk.Label(window, text="Enter Length").pack()
value_entry = tk.Entry(window)
value_entry.pack()

tk.Label(window, text="From").pack()
from_var = tk.StringVar()
from_var.set("Inches")
from_menu = tk.OptionMenu(window, from_var,
                          "Inches", "Centimeters", "Meters", "Kilometers")
from_menu.pack()

tk.Label(window, text="To").pack()
to_var = tk.StringVar()
to_var.set("Centimeters")
to_menu = tk.OptionMenu(window, to_var,
                        "Inches", "Centimeters", "Meters", "Kilometers")
to_menu.pack()

tk.Button(window, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()