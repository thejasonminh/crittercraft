import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import random

class MemorizationGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memorization Game")

        # Initialize sequences
        self.sequence = []
        self.player_sequence = []

        critterfont = font.Font(family = "Helvetica")
        critterFont = font.Font(size = 20)

        # Create buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        # Up and Down buttons
        self.btUp = tk.Button(button_frame, text="Up", command=lambda: self.add_to_player_sequence("Up"))
        self.btUp.grid(row=0, column=1, pady=5)
        self.btUp['font'] = critterfont

        self.btDown = tk.Button(button_frame, text="Down", command=lambda: self.add_to_player_sequence("Down"))
        self.btDown.grid(row=2, column=1, pady=5)
        self.btDown['font'] = critterfont

        # Left and Right buttons
        self.btLeft = tk.Button(button_frame, text="Left", command=lambda: self.add_to_player_sequence("Left"))
        self.btLeft.grid(row=1, column=0, padx=5)
        self.btLeft['font'] = critterfont

        self.btRight = tk.Button(button_frame, text="Right", command=lambda: self.add_to_player_sequence("Right"))
        self.btRight.grid(row=1, column=2, padx=5)
        self.btRight['font'] = critterfont

        # Start and Submit buttons
        start_button = tk.Button(button_frame, text="Start", command=self.start_game)
        start_button.grid(row=1, column=1, pady=10)
        start_button['font'] = critterfont

        submit_button = tk.Button(button_frame, text="Submit", command=self.check_sequence)
        submit_button.grid(row=3, column=1)
        submit_button['font'] = critterfont

        # Disable buttons initially
        self.disable_buttons()

    def disable_buttons(self):
        for direction in ["Left", "Right", "Up", "Down"]:
            self.get_button(direction).config(state=tk.DISABLED)

    def enable_buttons(self):
        for direction in ["Left", "Right", "Up", "Down"]:
            self.get_button(direction).config(state=tk.NORMAL)

    def add_to_player_sequence(self, direction):
        self.player_sequence.append(direction)

    def start_game(self):
        self.sequence = []
        self.player_sequence = []
        self.disable_buttons()
        self.generate_sequence()
        self.show_sequence()
        self.enable_buttons()

    def generate_sequence(self):
        directions = ["Left", "Right", "Up", "Down"]
        for i in range(5):  # Adjust the number of moves in the sequence as needed
            self.sequence.append(random.choice(directions))

    def show_sequence(self):
        print(self.sequence)
        for i, direction in enumerate(self.sequence):
            self.master.after(i * 1500, lambda d=direction: self.highlight_button(d))
            self.master.after((i + 1) * 2200, self.clear_highlight)

    def highlight_button(self, direction):
        self.get_button(direction).config(bg="red")

    def clear_highlight(self):
        for direction in ["Left", "Right", "Up", "Down"]:
            self.get_button(direction).config(bg="")

    def check_sequence(self):
        print(self.player_sequence)
        if self.player_sequence == self.sequence:
            messagebox.showinfo("Success", "Correct sequence! You won!")
        else:
            messagebox.showerror("Error", "Incorrect sequence. Try again.")
        self.disable_buttons()
        self.sequence = []
        self.player_sequence = []

    def get_button(self, direction):
        if direction == "Up":
            return self.btUp
        elif direction == "Down":
            return self.btDown
        elif direction == "Left":
            return self.btLeft
        elif direction == "Right":
            return self.btRight

if __name__ == "__main__":
    root = tk.Tk()
    game = MemorizationGame(root)
    root.mainloop()