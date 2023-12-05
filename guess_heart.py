import random
import tkinter as tk
from tkinter import messagebox

# Create class for the Heart Guessing Game
class HeartGuessing:
    def __init__(self, master):
        # Initalize game
        self.master = master
        self.master.title("Guess the Number of Hearts Game")

        # Generate a random number of hearts from 1-10
        self.no_of_hearts = random.randint(1, 10)
        self.attempts = 0
        self.no_of_attempts = 3 # Number of allowed attempts for player

        # Add GUI components
        self.label = tk.Label(
            master, text="Enter your guess for the number of hearts ❤️ (enter a number from 1-10):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(
            master, text="Guess", command=self.guess_hearts)
        self.guess_button.pack()

    # Handle the user's guess
    def guess_hearts(self):
        try:
            guess = int(self.entry.get())
            self.check_guess(guess)
        # Display an error message if the user's input is not a valid number
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    # Check the user's guess
    def check_guess(self, guess):
        self.attempts += 1

        if guess == self.no_of_hearts:
            # Display message to inform win if user guesses correctly
            messagebox.showinfo(message=f"Congratulations You guessed {self.no_of_hearts} number of hearts in {self.attempts} attempts. You earned 1 ❤️")
            self.master.destroy()
            exit()
        elif guess < self.no_of_hearts:
            # Prompt the user to go higher if the guess is too low
            messagebox.showinfo("Incorrect", "Try again. Go higher.")
        else:
            # Prompt the user to go lower if the guess is too high
            messagebox.showinfo("Incorrect", "Try again. Go lower.")

        if self.attempts == self.no_of_attempts:
            # Display message to inform user if they are out of attempts
            messagebox.showinfo(message=f"Sorry, you've out of attempts. The correct number of hearts was {self.no_of_hearts} ❤️.")
            self.master.destroy()

# Function to run game
def main():
    root = tk.Tk()
    game = HeartGuessing(root)
    root.mainloop()

# Entry point of program
if __name__ == "__main__":
    main()
