import tkinter as tk
from tkinter import messagebox
import random
import time


class TicTacBoneGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Bone")

        self.players_symbol = {"X": "\U0001F984", "O": "\U0001F43E"}
        self.user = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = [[None, None, None], [
            None, None, None], [None, None, None]]
        self.current_player = "X"

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(
                    self.window, text="", font=("Arial", 24),
                    width=5, height=2, command=lambda row=i, column=j: self.on_click(row, column)
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.computer = "O"
        self.user_turn = True

        self.window.mainloop()

    def on_click(self, row, column):
        if self.user_turn and self.board[row][column] == "" and not self.winner_check():
            self.user_turn = False
            self.board[row][column] = self.current_player
            self.button_update(row, column)

            if self.winner_check():
                tkinter.messagebox.showinfo("You earn 1 \U0001F984!")
                self.game_reset()
            elif self.tie_check():
                tkinter.messagebox.showinfo(
                    "It's a tie! Play again to earn \U0001F984")
                self.game_reset()
            else:
                self.window.after(1000, self.computer_turn)

    def button_update(self, row, column):
        symbol = self.players_symbol.get(self.current_player, "")
        self.buttons[row][column].config(text=symbol, state=DISABLED)

    def winner_check(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def tie_check(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def game_reset(self):
        self.window.destroy()
        start_new_game = TicTacBoneGUI()

    def computer_turn(self):
        empty_slot = [(i, j) for i in range(3)
                      for j in range(3) if self.board[i][j] == ""]
        if empty_slot:
            row, column = random.choice(empty_slot)
            self.board[row][column] = "O"
            self.button_update(row, column)

            if self.winner_check():
                tkinter.messagebox.showinfo(
                    "You lost! Play again to earn \U0001F984")
                self.game_reset()
            elif self.tie_check():
                tkinter.messagebox.showinfo(
                    "It's a tie! Play again to earn \U0001F984")
                self.game_reset()
            else:
                self.current_player = "X"
                self.user_turn = True


TicTacBoneGUI()
