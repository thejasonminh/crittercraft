from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
import random
import time


class TicTacBoneGUI:
    def __init__(self):
        self.window = Tk()  # Create a window
        self.window.title("Tic-Tac-Bone")

        self.players_symbol = {"X": "🦴", "O": "🐾"}  # Map symbols to emojis

        # Initialize symbol for the use
        self.user = "X"
        # Initialize the tictacbone board
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

        # Initatlize list to store buttons
        self.buttons = [[None, None, None], [
            None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                # Create buttons for tictacbone grid
                self.buttons[i][j] = Button(self.window, text="", font=("Arial", 24),
                                            width=5, height=2, command=lambda row=i, column=j: self.on_click(row, column))
                # Put buttons in the grid
                self.buttons[i][j].grid(row=i, column=j)

        self.computer = "0"  # Initalize symbol for computer
        self.user_turn = True  # Track whether it is the player's turn

        self.window.mainloop()

    def on_click(self, row, column):
        # Player's turn when player can click, button is empty, and there is no winner yet
        if self.user_turn and self.board[row][column] == "" and not self.check_winner():
            # Player prevented from playing when computer's turn
            self.user_turn = False
            # Update board with the current player's symbol
            self.board[row][column] = self.current_player
            # Update onto the corresponding button on the board
            self.button_update

        if self.winner_check():
            tkinter.messagebox.showresult(print("You earn 1 🦴!"))
            self.game_reset()
        elif self.tie_check():
            tkinter.messagebox.showresult("It's a tie! Play again to earn 🦴")
        else:
            self.current_player = ""

            if self.current_player == self.computer:
                time.sleep(1)
                self.computer_turn()

    def button_update(self, row, column):
        # Get current player's symbol
        symbol = self.players_symbol.get(self.current_player, "")
        # Update button and disable it
        self.buttons[row][column].config(text=symbol, state=Tk.DISABLED)


TicTacBoneGUI()  # Create GUI
