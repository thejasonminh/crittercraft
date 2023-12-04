from tkinter import *
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

        self.critterfont = font.Font(family = "Helvetica")
        self.critterFont = font.Font(size = 20)
        
        # Create labels
        label_frame = Frame(self.master)
        label_frame.pack(pady=10)

        self.lbWelcome = Label(label_frame, text="Welcome to Memorize Me!").grid(row=0, column=1)
        self.lbInstructions = Label(label_frame, text="Press start to see the pattern, memorize and copy it, and click submit.").grid(row=1, column=1)
        self.statusVar = StringVar()
        self.statusVar.set("Press start!")
        self.lbStatus = Label(label_frame, textvariable = self.statusVar, fg = 'blue').grid(row=3, column=1)

        # Create buttons
        button_frame = Frame(self.master)
        button_frame.pack(pady=10)

        # Up and Down buttons
        self.btUp = Button(button_frame, text="Up", command=lambda: self.add_to_player_sequence("Up"))
        self.btUp.grid(row=0, column=1, pady=5)
        self.btUp['font'] = self.critterfont

        self.btDown = Button(button_frame, text="Down", command=lambda: self.add_to_player_sequence("Down"))
        self.btDown.grid(row=2, column=1, pady=5)
        self.btDown['font'] = self.critterfont

        # Left and Right buttons
        self.btLeft = Button(button_frame, text="Left", command=lambda: self.add_to_player_sequence("Left"))
        self.btLeft.grid(row=1, column=0, padx=5)
        self.btLeft['font'] = self.critterfont

        self.btRight = Button(button_frame, text="Right", command=lambda: self.add_to_player_sequence("Right"))
        self.btRight.grid(row=1, column=2, padx=5)
        self.btRight['font'] = self.critterfont

        # Start and Submit buttons
        start_button = Button(button_frame, text="Start", command=self.start_game)
        start_button.grid(row=1, column=1, pady=10)
        start_button['font'] = self.critterfont

        submit_button = Button(button_frame, text="Submit Sequence", command=self.check_sequence)
        submit_button.grid(row=3, column=1)
        submit_button['font'] = self.critterfont

        # Disable buttons initially
        self.disable_buttons()

    def disable_buttons(self):
        for direction in ["Left", "Right", "Up", "Down"]:
            self.get_button(direction).config(state=DISABLED)

    def enable_buttons(self):
        for direction in ["Left", "Right", "Up", "Down"]:
            self.get_button(direction).config(state=NORMAL)

    def add_to_player_sequence(self, direction):
        self.player_sequence.append(direction)

    def start_game(self):
        self.statusVar.set("Wait and watch... When the pattern finishes, repeat it, and press submit!")
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
        for i, direction in enumerate(self.sequence):
            self.master.after(i * 1500, lambda d=direction: self.highlight_button(d))
            self.master.after((i + 1) * 1800, self.clear_highlight)

    def highlight_button(self, direction):
        self.get_button(direction).config(fg="red")

    def clear_highlight(self):
        for direction in ["Left", "Right", "Up", "Down"]:
            self.get_button(direction).config(fg="black")

    def check_sequence(self):
        if self.player_sequence == self.sequence:
            messagebox.showinfo("Success", "Correct sequence! You won!")
            self.master.destroy()
        else:
            messagebox.showerror("Error", "Incorrect sequence. Try again.")
            self.master.destroy()
        self.statusVar.set("Press start!")
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
    root = Tk()
    game = MemorizationGame(root)
    root.mainloop()