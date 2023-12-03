import tkinter as tk
from tkinter import messagebox
import random


class HeartGuessing:
    def __init__(self, master):
        self.master = master
        self.master.title("Number of Hearts")

        self.secret_number = random.randint(1, 10)
        self.attempts = 0
        self.no_of_attempts = 5

        self.label = tk.Label(
            master, text="Enter your guess for the number of hearts (enter a number from 1-10):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(
            master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def make_guess(self):
        try:
            guess = int(self.entry.get())
            self.check_guess(guess)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def check_guess(self, guess):
        self.attempts += 1

        if guess == self.secret_number:
            messagebox.showinfo(message=f"Congratulations, you guessed correctly! You gained {
                                self.secret_number} hearts in {self.attempts} attempts.")
            self.master.destroy()
        elif guess < self.secret_number:
            messagebox.showinfo("Incorrect", "Try again. Go higher.")
        else:
            messagebox.showinfo("Incorrect", "Try again. Go lower.")

        if self.attempts == self.no_of_attempts:
            messagebox.showinfo(message=f"Game Over! Sorry, you've run out of attempts. The correct number of hearts was" {self.secret_number}.)
            self.master.destroy()


def main():
    root = tk.Tk()
    game = HeartGuessing(root)
    root.mainloop()


if __name__ == "__main__":
    main()
