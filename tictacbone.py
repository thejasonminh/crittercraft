import tkinter as tk
from tkinter import messagebox  # Import tkinter.messagebox
import random
import time


class TicTacBoneGUI:
    def __init__(self):  # Set up intial state of tictacbone
        self.window = tk.Tk()  # Create a window
        self.window.title("Tic-Tac-Bone")  # Set window title

        # Initialize the tictacbone board as a 3 by 3 grid
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        # Initialize list to store buttons
        self.buttons = [[None, None, None], [
            None, None, None], [None, None, None]]
        # ADD COMMENT
        self.current_player = "X"

        # ADD COMMENT
        for i in range(3):
            for j in range(3):
                # Create buttons for tictacbone grid
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Arial", 24),
                                               width=5, height=2, command=lambda row=i, column=j: self.on_click(row, column))
                # Put buttons in the grid
                self.buttons[i][j].grid(row=i, column=j)

        self.computer = "O"  # Initalize symbol for computer
        self.user_turn = True  # Track whether it is the player's turn

        self.window.mainloop()

    def on_click(self, row, column):
        # Player's turn when player can click, button is empty, and there is no winner yet
        if self.user_turn and self.board[row][column] == "" and not self.winner_check():
            # Player prevented from playing when computer's turn
            self.user_turn = False
            # Update board with the current player's symbol
            self.board[row][column] = self.current_player
            # Update onto the corresponding button on the board
            self.button_update(row, column)

            if self.winner_check():
                # Sends message to show win if player wins
                messagebox.showinfo(title="TicTacBone",
                                    message="You earn 1 🦴!")
                self.game_reset()  # Resets the game
            elif self.tie_check():
                # Sends message to show tie if result is a tie
                messagebox.showinfo(
                    title="TicTacBone", title="TicTacBone", message="It's a tie! Play again to earn 🦴")
                self.game_reset()  # Reset the game
            else:
                self.current_player = self.computer  # If it is currently the computer's turn
                time.sleep(1)  # Add delay
                self.computer_turn()  # And allow computer to make computer's move

    def button_update(self, row, column):
        # Change symbols to bone and paw
        symbol = "🦴" if self.current_player == "X" else "🐾"
        # Update button and disable it
        self.buttons[row][column].config(text=symbol, state=tk.DISABLED)

    def winner_check(self):
        for i in range(3):
            # Horizontal: check if all symbols in the current row are the same and not empty
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True  # TRUE if row has the same elements and is not empty

            # Vertical: check if all symbols in the current column are the same and not empty
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True  # TRUE if column has the same elements and is not empty

        # Diagonal: check if all symbols top-left to bottom-right are the same and not empty
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True  # TRUE if diagonal from top-left to bottom-right has the same elements and is not empty

        # Diagonal: check if all symbols top-right to bottom-left are the same and not empty
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True  # TRUE if diagonal from top-right to bottom-left has the same elements and is not empty

        # If none of the conditions above are met, meaning no one has won, return False
        return False  # False if there is not a winning condition

    def tie_check(self):
        # Iterate over rows and columns
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":  # Check for empty slot
                    return False  # Game is not a tie if there is an empty slot
        return True  # Game is a tie if no empty slot are found

    def game_reset(self):
        self.window.destroy()  # Close the window
        start_new_game = TicTacBoneGUI()  # Start a new game

    def computer_turn(self):
        # Look for empty slots in the 3 by 3 grid
        empty_slot = [(i, j) for i in range(3)
                      for j in range(3) if self.board[i][j] == ""]

        # Choose empty slot randomly
        if empty_slot:
            row, column = random.choice(empty_slot)
            # Place symbol for computer in randomly chosen slot
            self.board[row][column] = "O"
            # Update onto the corresponding button on the board
            self.button_update(row, column)

            # Check for potential win by computer
            if self.winner_check():
                messagebox.showinfo(title="TicTacBone",
                                    message="You lost! Play again to earn 🦴")
                self.game_reset()  # Reset the game
            # Check for a tie
            elif self.tie_check():
                # Sends message to show tie if result is a tie
                messagebox.showinfo(title="TicTacBone",
                                    message="It's a tie! Play again to earn 🦴")
                self.game_reset()  # Reset the game
            # Else, allow user to conduct their next turn
            else:
                self.current_player = "X"
                self.user_turn = True


if __name__ == "__main__":
    TicTacBoneGUI()  # Create GUI
