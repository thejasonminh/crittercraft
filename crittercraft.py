# Author: Jason Ngo, Jayden Jung, Jueun Kang
# Class: INF 0452H; Information Design Studio V: Coding
# Instructor: Maher Elshakankiri
# Assignment: Final Project
# Date Created: 11/25/2023
# Last Modified: 11/25/2023
# Purpose: CritterCraft

from tkinter import * # Import tkinter
from pathlib import Path 
import tkinter.font as font

p = Path(__file__)
print(p.parent)

class crittercraft():
    def __init__ (self):
        window = Tk()
        window.title("CritterCraft")

        critterFont = font.Font(family = "Helvetica")
        critterFont = font.Font(size = 30)

        self.canvas = Canvas(window, width = 800, height = 800, bg = "white")
        self.canvas.pack()

        self.logoImage = PhotoImage(file = f"{p.parent}\cclogo.png")

        self.canvas.create_image(400, 200, image = self.logoImage, tag = "logo")
        btn_next = Button(window, text = "Create Your Critter!", bg = "#8cc45c")
        btn_next['font'] = critterFont
        self.canvas.create_window(400, 600, window = btn_next)
        window.mainloop()

crittercraft()