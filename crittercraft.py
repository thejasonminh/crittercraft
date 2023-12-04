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
import threading

p = Path(__file__)
print(p.parent)

class crittercraft():
    def __init__ (self):
        ## Initializing window and titling it
        self.window = Tk()
        self.window.title("CritterCraft")

        ## Initializing attributes for critter
        self.critterName = StringVar()
        self.critterType = ""
        self.critterHealth = 2
        self.critterLove = 2
        self.critterHun = 2
        self.critterHealthMax = 3
        self.critterLoveMax = 3
        self.critterHunMax = 3
        self.yourCritterName = ""
        self.yourCritter = ""

        ## Creating font settings 
        self.critterFont = font.Font(family = "Helvetica")
        self.critterFont = font.Font(size = 30)

        ## Creating a canvas that will have everything inside
        self.canvas = Canvas(self.window, width = 800, height = 800, bg = "white")
        self.canvas.pack()

        ## Loading logo image
        self.logoImage = PhotoImage(file = f"{p.parent}/cclogo.png")

        ## Sheep Pictures
        self.black_sheep = PhotoImage(file = f"{p.parent}/sheep_black.png")
        self.white_sheep = PhotoImage(file = f"{p.parent}/sheep_white.png")
        self.pink_sheep = PhotoImage(file = f"{p.parent}/sheep_pink.png")
        ## Resize Pictures
        self.white_sheep = self.white_sheep.zoom(25)
        self.white_sheep = self.white_sheep.subsample(60)
        self.black_sheep = self.black_sheep.zoom(25)
        self.black_sheep = self.black_sheep.subsample(60)
        self.pink_sheep = self.pink_sheep.zoom(25)
        self.pink_sheep = self.pink_sheep.subsample(60)

        ## Duck Pictures
        self.yellow_duck = PhotoImage(file = f"{p.parent}/duck_yellow.png")
        self.white_duck = PhotoImage(file = f"{p.parent}/duck_white.png")
        self.pink_duck = PhotoImage(file = f"{p.parent}/duck_pink.png")
        ## Resize pictures
        self.white_duck = self.white_duck.zoom(25)
        self.white_duck = self.white_duck.subsample(60)
        self.yellow_duck = self.yellow_duck.zoom(25)
        self.yellow_duck = self.yellow_duck.subsample(60)
        self.pink_duck = self.pink_duck.zoom(25)
        self.pink_duck = self.pink_duck.subsample(60)

        ## Panda Pictures
        self.pink_panda = PhotoImage(file = f"{p.parent}/panda_pink.png")
        self.red_panda = PhotoImage(file = f"{p.parent}/panda_red.png")
        self.white_panda = PhotoImage(file = f"{p.parent}/panda_white.png")
        ## Resize Pictures
        self.white_panda = self.white_panda.zoom(25)
        self.white_panda = self.white_panda.subsample(60)
        self.red_panda = self.red_panda.zoom(25)
        self.red_panda = self.red_panda.subsample(60)
        self.pink_panda = self.pink_panda.zoom(25)
        self.pink_panda = self.pink_panda.subsample(60)

        # Background pictures
        self.bg_default = PhotoImage(file = f"{p.parent}/bg_default.png")
        # self.bg_death = PhotoImage(file = f"{p.parent}/bg_death.png")
        # Resize
        # self.bg_default = self.bg_default.zoom(1)
        # self.bg_default = self.bg_default.subsample(60)
        # self.bg_death = self.bg_death.zoom(25)
        # self.bg_death = self.bg_death.subsample(60)

        ## Drawing the image into the canvas
        self.canvas.create_image(400, 300, image = self.logoImage, tag = "logo")

        ## Make buttons to select critter
        self.btn_Sheep = Button(self.window, text = "Sheep!", font = self.critterFont, bg = "#8cc45c", command = self.sheepColor)
        self.btn_Duck = Button(self.window, text = "Duck!", font = self.critterFont, bg = "#8cc45c", command = self.duckColor)
        self.btn_Panda = Button(self.window, text = "Panda!", font = self.critterFont, bg = "#8cc45c", command = self.pandaColor)

        ## Make Radio Buttons to select color per critter
        self.colorchoice = IntVar()
        self.rbPandaWhite = Radiobutton(self.window, text = "White", font = self.critterFont, variable = self.colorchoice, value = 1)
        self.rbPandaPink = Radiobutton(self.window, text = "Pink", font = self.critterFont, variable = self.colorchoice, value = 2)
        self.rbPandaRed = Radiobutton(self.window, text = "Red", font = self.critterFont, variable = self.colorchoice, value = 3)

        self.rbSheepWhite = Radiobutton(self.window, text = "White", font = self.critterFont, variable = self.colorchoice, value = 1)
        self.rbSheepPink = Radiobutton(self.window, text = "Pink", font = self.critterFont, variable = self.colorchoice, value = 2)
        self.rbSheepBlack = Radiobutton(self.window, text = "Black", font = self.critterFont, variable = self.colorchoice, value = 3)

        self.rbDuckWhite = Radiobutton(self.window, text = "White", font = self.critterFont, variable = self.colorchoice, value = 1)
        self.rbDuckYellow = Radiobutton(self.window, text = "Yellow", font = self.critterFont, variable = self.colorchoice, value = 2)
        self.rbDuckPink = Radiobutton(self.window, text = "Pink", font = self.critterFont, variable = self.colorchoice, value = 3)

        ## Button to confirm color select
        self.btn_confirmColor = Button(self.window, text = "Confirm!", font = self.critterFont, bg = "#8cc45c", command = self.confirmColor)
        
        ## Make a back button
        self.btn_back = Button(self.window, text = "Back", font = self.critterFont, bg = "#8cc45c", command = self.createCritter) 

        ## Make a text entry field
        self.critterNameEntry = Entry(self.window, textvariable = self.critterName)

        ## Button to confirm name
        self.getName = Button(self.window, text = "Confirm Name", font = self.critterFont, bg = "#8cc45c", command = self.namePress)
        
        ## Creating an action button, text based on the font settings defined earlier
        self.btn_next = Button(self.window, text = "Create Your Critter!", font = self.critterFont, bg = "#8cc45c", command = self.createCritter)

        self.gotoHubBtn = Button(self.window, text = "Confirm Name", font = self.critterFont, bg = "#8cc45c", command = self.goHub)
        
        ## Add button to the canvas
        self.canvas.create_window(400, 600, window = self.btn_next)

        self.window.mainloop()

    ## Method that represents the next screen
    def createCritter(self):
        
        ## Clear the screen
        self.canvas.delete("all")

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = "Choose Your Critter!", font = "Helvetica 30")

        ## Create images of the 3 animals
        self.canvas.create_image(200, 400, image = self.white_sheep, tag = "wsheep")
        self.canvas.create_image(400, 400, image = self.white_duck, tag = "wduck")
        self.canvas.create_image(600, 400, image = self.white_panda, tag = "wpanda")

        ## Load buttons
        self.canvas.create_window(200, 600, window = self.btn_Sheep)
        self.canvas.create_window(400, 600, window = self.btn_Duck)
        self.canvas.create_window(600, 600, window = self.btn_Panda)

    def pandaColor(self):
        ## Assign critter type
        self.critterType = "Panda"

        ## Clear the screen
        self.canvas.delete("all")

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = "Choose Your Color!", font = "Helvetica 30")

        ## Create images of the 3 pandas
        self.canvas.create_image(200, 400, image = self.white_panda, tag = "wpanda")
        self.canvas.create_image(400, 400, image = self.pink_panda, tag = "ppanda")
        self.canvas.create_image(600, 400, image = self.red_panda, tag = "rpanda")

        ## Load Radio Buttons
        self.canvas.create_window(200, 600, window = self.rbPandaWhite)
        self.canvas.create_window(400, 600, window = self.rbPandaPink)
        self.canvas.create_window(600, 600, window = self.rbPandaRed)

        self.canvas.create_window(400, 700, window = self.btn_confirmColor)

        self.canvas.create_window(100, 75, window = self.btn_back)
    
    def sheepColor(self):
        ## Assign critter type
        self.critterType = "Sheep"

        ## Clear the screen
        self.canvas.delete("all")

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = "Choose Your Color!", font = "Helvetica 30")

        ## Create images of the 3 sheeps
        self.canvas.create_image(200, 400, image = self.white_sheep, tag = "wsheep")
        self.canvas.create_image(400, 400, image = self.pink_sheep, tag = "psheep")
        self.canvas.create_image(600, 400, image = self.black_sheep, tag = "bsheep")

        ## Load Radio Buttons
        self.canvas.create_window(200, 600, window = self.rbSheepWhite)
        self.canvas.create_window(400, 600, window = self.rbSheepPink)
        self.canvas.create_window(600, 600, window = self.rbSheepBlack)

        self.canvas.create_window(400, 700, window = self.btn_confirmColor)

        self.canvas.create_window(100, 75, window = self.btn_back)

    def duckColor(self):
        ## Assign critter type
        self.critterType = "Duck"

        ## Clear the screen
        self.canvas.delete("all")

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = "Choose Your Color!", font = "Helvetica 30")

        ## Create images of the 3 ducks
        self.canvas.create_image(200, 400, image = self.white_duck, tag = "wduck")
        self.canvas.create_image(400, 400, image = self.yellow_duck, tag = "yduck")
        self.canvas.create_image(600, 400, image = self.pink_duck, tag = "pduck")

        ## Load Radio Buttons
        self.canvas.create_window(200, 600, window = self.rbDuckWhite)
        self.canvas.create_window(400, 600, window = self.rbDuckYellow)
        self.canvas.create_window(600, 600, window = self.rbDuckPink)

        self.canvas.create_window(400, 700, window = self.btn_confirmColor)

        self.canvas.create_window(100, 75, window = self.btn_back)

    def confirmColor(self):
        if self.critterType == "Panda":
            if self.colorchoice.get() == 1:
                print("white panda")
                self.yourCritter = self.white_panda
            elif self.colorchoice.get() == 2:
                print("pink panda")
                self.yourCritter = self.pink_panda
            else:
                print("red panda")
                self.yourCritter = self.red_panda
        elif self.critterType == "Sheep":
            if self.colorchoice.get() == 1:
                print("white sheep")
                self.yourCritter = self.white_sheep
            elif self.colorchoice.get() == 2:
                print("pink sheep")
                self.yourCritter = self.pink_sheep
            else:
                print("black sheep")
                self.yourCritter = self.black_sheep
        elif self.critterType == "Duck":
            if self.colorchoice.get() == 1:
                print("white duck")
                self.yourCritter = self.white_duck
            elif self.colorchoice.get() == 2:
                print("yellow duck")
                self.yourCritter = self.yellow_duck
            else:
                print("pink duck")
                self.yourCritter = self.pink_duck
        self.typeName()

    def typeName(self):
        ## Clear the screen
        self.canvas.delete("all")

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = "Name Your Critter!", font = "Helvetica 30")

        ## Display the critter you chose
        self.canvas.create_image(400, 300, image = self.yourCritter)

        ## Add text entry
        self.canvas.create_window(400, 600, window = self.critterNameEntry)

        ## Add button to confirm
        self.canvas.create_window(400, 700, window = self.getName)

        self.canvas.create_window(100, 75, window = self.btn_back)

    def namePress(self):
        ## Clear the screen
        self.canvas.delete("all")
        self.yourCritterName = self.critterName.get()

        # Display background
        # self.canvas.create_image(400, 400, image = self.bg_default)

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")
        ## Adding  text to the header
        self.canvas.create_text(400, 75, text = f"{self.yourCritterName}", font = "Helvetica 30")

        ## Display the critter you chose
        self.canvas.create_image(400, 475, image = self.yourCritter)

        self.canvas.create_window(400, 700, window = self.gotoHubBtn)

        self.canvas.create_window(100, 75, window = self.btn_back)

    def goHub(self):
        ## Clear the screen
        self.canvas.delete("all")
        self.canvas.create_image(400, 400, image = self.bg_default)

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")

        ## Fill attributes in the rectangle
        self.canvas.create_text(400, 40, text = f"{self.yourCritterName}", font = "Helvetica 30")
        self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20")
        self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20")
        self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20")

        self.canvas.create_image(400, 475, image = self.yourCritter)
        

crittercraft()