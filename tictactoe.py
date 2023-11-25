import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeComputerPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe - Bone Theme")

        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Helvetica", 24),
                                               width=5, height=2, command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.computer_player = "O"
        self.user_can_click = True  # Flag to control user input

    def on_click(self, row, col):
        if self.user_can_click and self.board[row][col] == "" and not self.check_winner():
            self.user_can_click = False  # Disable user input during computer's turn
            self.board[row][col] = self.current_player
            self.update_button(row, col)

            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

                if self.current_player == self.computer_player:
                    # After a delay, enable user input and let the computer make its move
                    self.window.after(1000, self.computer_move)

    def update_button(self, row, col):
        symbol = "🦴" if self.current_player == "X" else "🐾"
        self.buttons[row][col].config(text=symbol, state=tk.DISABLED)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True  # Check rows
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True  # Check columns

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True  # Check diagonal from top-left to bottom-right
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True  # Check diagonal from top-right to bottom-left

        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="", state=tk.NORMAL)
        self.user_can_click = True  # Reset user input flag

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.computer_player
            self.update_button(row, col)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.computer_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "X"
                self.user_can_click = True  # Enable user input for the next turn

if __name__ == "__main__":
    game = TicTacToeComputerPlayer()
    game.window.mainloop()
