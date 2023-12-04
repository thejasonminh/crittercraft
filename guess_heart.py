import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")

        self.secret_number = random.randint(1, 10)
        print(self.secret_number)
        self.attempts = 0
        self.max_attempts = 3

        self.label = tk.Label(master, text="Enter your guess (1-10):")
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
            messagebox.showinfo(message = f"Congratulations You guessed the number {self.secret_number} in {self.attempts} attempts.")
            self.master.destroy()
            exit()
        elif guess < self.secret_number:
            messagebox.showinfo("Incorrect", "Try again. Go higher.")
        else:
            messagebox.showinfo("Incorrect", "Try again. Go lower.")

        if self.attempts == self.max_attempts:
            messagebox.showinfo(message = f"Game Over, Sorry, you've run out of attempts. The correct number was {self.secret_number}.")
            self.master.destroy()


def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()