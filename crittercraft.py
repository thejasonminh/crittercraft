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
        ## Initializing window and titling it
        window = Tk()
        window.title("CritterCraft")

        ## Creating font settings 
        critterFont = font.Font(family = "Helvetica")
        critterFont = font.Font(size = 30)

        ## Creating a canvas that will have everything inside
        self.canvas = Canvas(window, width = 800, height = 800, bg = "white")
        self.canvas.pack()

        ## Loading logo image
        self.logoImage = PhotoImage(file = f"{p.parent}/cclogo.png")

        ## Drawing the image into the canvas
        self.canvas.create_image(400, 300, image = self.logoImage, tag = "logo")
        
        ## Creating an action button, text based on the font settings defined earlier
        btn_next = Button(window, text = "Create Your Critter!", bg = "#8cc45c", command = self.createCritter)
        btn_next['font'] = critterFont
        
        ## Add button to the canvas
        self.canvas.create_window(400, 600, window = btn_next)

        window.mainloop()

    ## Method that represents the next screen
    def createCritter(self):
        
        ## Clear the screen
        self.canvas.delete("all")
        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "yellow")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = "Choose Your Critter!", fill = "#8cc45c", font = "Helvetica 30")

        ## CODE TO BE ADDED
        # Load the 9 images of the possible critters
        # First, draw out 3 images of the "types" of critters we have (sheep, duck, panda)
        # Upon selection, ask the user to select the color variant of each critter
        # AFTERWARDS, name it and then proceed to the main body of the game, but that can wait

crittercraft()