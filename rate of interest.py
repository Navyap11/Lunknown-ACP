import tkinter as tk

def calculate():
    principal = float(principal_entry.get())
    months = float(time_entry.get())
    rate = float(rate_entry.get())

    simple_interest = (principal * rate * months) / 100
    compound_interest = principal * (1 + rate / 100) ** months - principal

    result_label.config(
        text="Simple Interest = " + str(round(simple_interest, 2)) +
        "\nCompound Interest = " + str(round(compound_interest, 2))
    )

window = tk.Tk()
window.title("Interest Calculator")
window.geometry("400x300")

tk.Label(window, text="Principal Amount").pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

tk.Label(window, text="Time Period (Months)").pack()
time_entry = tk.Entry(window)
time_entry.pack()

tk.Label(window, text="Rate of Interest (%)").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

tk.Button(window, text="Calculate Interest", command=calculate).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()