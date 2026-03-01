import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    user_choice_label.config(text="Your Choice: " + user_choice)
    computer_choice_label.config(text="Computer Choice: " + computer_choice)
    result_label.config(text=result)
    score_label.config(
        text=f"Score - You: {user_score}  Computer: {computer_score}"
    )

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x400")
window.resizable(False, False)

title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(
    button_frame,
    text="Rock",
    width=10,
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
    button_frame,
    text="Paper",
    width=10,
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    width=10,
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(window, text="Your Choice: ")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(window, text="Computer Choice: ")
computer_choice_label.pack(pady=5)

result_label = tk.Label(
    window,
    text="Make your move!",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

score_label = tk.Label(
    window,
    text="Score - You: 0  Computer: 0"
)
score_label.pack(pady=10)

window.mainloop()