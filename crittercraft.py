# Author: Jason Ngo, Jayden Jung, Jueun Kang
# Class: INF 0452H; Information Design Studio V: Coding
# Instructor: Maher Elshakankiri
# Assignment: Final Project
# Date Created: 11/25/2023
# Last Modified: 11/25/2023
# Purpose: CritterCraft

from tkinter import * # Import tkinter
from tkinter import messagebox
from pathlib import Path 
import pygame.mixer
from pygame.locals import *
import tkinter.font as font
import time
import threading
import random
import sys

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
        self.critterHealth = 3
        self.critterLove = 3
        self.critterHun = 3
        self.critterHealthMax = 4
        self.critterLoveMax = 4
        self.critterHunMax = 4
        self.yourCritterName = ""
        self.yourCritter = ""

        # Flag to activate internal timer. 0 = run, 1 = stop
        self.activeTimer = 0

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
        self.bg_death = PhotoImage(file = f"{p.parent}/bg_death.png")
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
    
        self.restartGame = Button(self.window, text = "Restart Game", font = self.critterFont, bg = "#8cc45c", command = self.resetGame)

        ## Add button to the canvas
        self.canvas.create_window(400, 600, window = self.btn_next)

        ## Make buttons to Care or Play with pet
        self.btn_care = Button(self.window, text = "Care", font = self.critterFont, bg = "#8cc45c", command = self.openCareWindow)
        self.btn_play = Button(self.window, text = "Play", font = self.critterFont, bg = "#8cc45c", command = self.openPlayWindow)

        # Game outcome value
        self.gameOutcome = 0

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
        internal_timer1 = threading.Timer(5.0, self.hubTimer)
        internal_timer1.start()

        self.activeTimer = 0

        ## Load music, and play it.
        pygame.mixer.init()
        pygame.mixer.music.load(f"{p.parent}/hub-music.mp3")
        pygame.mixer.music.play(loops = -1)

        ## Play emergency music if critter is about to die
        if self.critterHealth == 1 or self.critterHun == 1 or self.critterLove == 1:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f"{p.parent}/hub-emergency-music.mp3")
            pygame.mixer.music.play(Loops = -1)

        ## When hitting a minigame button, call threading.Timer.cancel()
        ## Clear the screen
        self.canvas.delete("all")
        self.canvas.create_image(400, 400, image = self.bg_default)

        ## Create a header rectangle
        self.canvas.create_rectangle(0, 0, 800, 150, fill = "#8cc45c")

        ## Fill attributes in the rectangle
        self.canvas.create_text(400, 40, text = f"{self.yourCritterName}", font = "Helvetica 30")
        self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20", tag = "hp")
        self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20", tag = "hgr")
        self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20", tag = "lov")

        self.canvas.create_image(400, 475, image = self.yourCritter)

        self.canvas.create_window(200, 600, window = self.btn_care)
        self.canvas.create_window(600, 600, window = self.btn_play)

    def openCareWindow(self):
        self.activeTimer = 1
        print("Care button pressed")
        careWindow = Toplevel(self.window)
        careWindow.title("Care")
        careWindow.geometry("200x100")
        framecare = Frame(careWindow) # Create and add a frame to window
        framecare.pack()
        btHealth = Button(framecare, text = "Clean", command=lambda: self.care(1, careWindow))
        btHealth.grid(row = 1, column = 1)
        btHunger = Button(framecare, text = "Feed", command=lambda: self.care(2, careWindow))
        btHunger.grid(row = 2, column = 1)
        btLove = Button(framecare, text = "Cuddle", command=lambda: self.care(3, careWindow))
        btLove.grid(row = 3, column = 1)

    def care(self, num, window):
        if num == 1:
            print("hp care")
            if self.critterHealth < self.critterHealthMax:
                self.critterHealth += 1
                self.canvas.delete("hp")
                self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20", tag = "hp")
            else:
                None
        elif num == 2: 
            print("hgr care")
            if self.critterHun < self.critterHunMax:
                self.critterHun += 1
                self.canvas.delete("hgr")
                self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20", tag = "hgr")
            else:
                None
        elif num == 3:
            print("lov care")
            if self.critterLove < self.critterLoveMax:
                self.critterLove += 1
                self.canvas.delete("lov")
                self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20", tag = "lov")
            else:
                None
        
        window.destroy()
        self.activeTimer = 0

    def openPlayWindow(self):
        self.activeTimer = 1
        gameswindow = Toplevel(self.window)
        gameswindow.title("Play")
        gameswindow.geometry("200x100")
        framegames = Frame(gameswindow) # Create and add a frame to window
        framegames.pack()
        btMem = Button(framegames, text = "Brain Booster!", 
                       command = lambda: self.game(1, gameswindow))
        btMem.grid(row = 1, column = 1)
        btTic = Button(framegames, text = "Tic Tac Bone!", 
                       command = lambda: self.game(2, gameswindow))
        btTic.grid(row = 2, column = 1)
        btGuess = Button(framegames, text = "Guess the love!", 
                         command = lambda: self.game(3, gameswindow))
        btGuess.grid(row = 3, column = 1)
    
    def game(self, num, window):
        window.destroy()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f"{p.parent}/minigame-music.mp3")
        pygame.mixer.music.play(loops = -1)
        self.gameOutcome = 0
        if num == 1:
            print("Memorization game")
            self.memGame()
            print(f"outcome: {self.gameOutcome}")
            if self.gameOutcome == 1:
                self.critterHealthMax += 1
                self.canvas.delete("hp")
                self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20", tag = "hp")
        elif num == 2:
            print("Bone game")
            self.boneGame()
            if self.gameOutcome == 1:
                self.critterHunMax += 1
                self.canvas.delete("hgr")
                self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20", tag = "hgr")
        elif num == 3:
            print("Love game")
            self.loveGame()
            if self.gameOutcome == 1:
                self.critterLoveMax += 1
                self.canvas.delete("lov")
                self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20", tag = "lov")
        window.destroy()
        self.activeTimer = 0
        self.gameOutcome = 0

    def memGame(self):
        print(self.gameOutcome)
        class MemorizationGame:
            def __init__(self):
                self.master = Tk()
                self.master.title("Brain Booster")

                self.outcome = 0

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
                self.master.mainloop()

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
                    messagebox.showinfo("Success", "Correct sequence! You won! Health max will increase by 1.")
                    print(3)
                    crittercraft.gameOutcome = 1
                    print(f"Game won. Outcome points: {crittercraft.gameOutcome}")
                    self.master.destroy()
                else:
                    messagebox.showerror("Error", "Incorrect sequence. Try again next time.")
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

        MemorizationGame()

    def boneGame(self):
        class TicTacBoneGUI:
            def __init__(self):  # Set up intial state of tictacbone
                self.window = Tk()  # Create a window
                self.window.title("Tic-Tac-Bone")  # Set window title

                # Initialize the tictacbone board as a 3 by 3 grid
                self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
                # Initialize list to store buttons
                self.buttons = [[None, None, None], [
                    None, None, None], [None, None, None]]
                # The current player is 'X'
                self.current_player = "X"
                # Store game outcome to 0 for on-going
                self.outcome = 0

                # Create buttons for the 3 by 3 tictacbone grid
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j] = Button(self.window, text="", font=("Arial", 24),
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
                        messagebox.showinfo(title = "TicTacBone", message = "Congratulations, you won! Hunger max will increase by 1.")
                        crittercraft.gameOutcome = 1
                        self.window.destroy() 
                    elif self.tie_check():
                        # Sends message to show tie if result is a tie
                        messagebox.showinfo(title = "TicTacBone", message = "It's a tie! Try again next time.")
                        self.window.destroy()
                    else:
                        self.current_player = self.computer  # If it is currently the computer's turn
                        self.computer_turn()  # And allow computer to make computer's move

            def button_update(self, row, column):
                # Change symbols to bone and paw
                symbol = "🦴" if self.current_player == "X" else "🐾"
                # Update button and disable it
                self.buttons[row][column].config(text=symbol, state=DISABLED)

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
                        messagebox.showinfo(title = "TicTacBone", message = "You lost! Try again next time.")
                        self.window.destroy()
                    # Check for a tie
                    elif self.tie_check():
                        # Sends message to show tie if result is a tie
                        messagebox.showinfo(title = "TicTacBone", message = "It's a tie! Try again next time.")
                        self.window.destroy()
                    # Else, allow user to conduct their next turn
                    else:
                        self.current_player = "X"
                        self.user_turn = True
        TicTacBoneGUI()

    def loveGame(self):
        class HeartGuessing:
            def __init__(self):
                # Initalize game
                self.master = Tk()
                self.master.title("Guess the Number of Hearts Game")

                # Generate a random number of hearts from 1-10
                self.no_of_hearts = random.randint(1, 10)
                self.attempts = 0
                self.no_of_attempts = 3 # Number of allowed attempts for player

                # Add GUI components
                self.label = Label(
                    self.master, text="Enter your guess for the number of hearts ❤️ (enter a number from 1-10):")
                self.label.pack()

                self.entry = Entry(self.master)
                self.entry.pack()

                self.guess_button = Button(
                    self.master, text="Guess", command=self.guess_hearts)
                self.guess_button.pack()

                self.window.mainloop()

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
                    messagebox.showinfo(message=f"Congratulations You guessed {self.no_of_hearts} number of hearts in {self.attempts} attempts. You win! Love max will increase by 1.")
                    crittercraft.gameOutcome = 1
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

    # Method that rolls random events designated to lower stats and kill the critter
    def hubTimer(self):
        internal_timer2 = threading.Timer(5.0, self.hubTimer)

        if self.activeTimer == 0:
            randStat = random.randint(0, 2)
            print(randStat)
            print("timer tick")
            ## Health goes down
            if randStat == 0:
                self.critterHealth -= 1
                if self.critterHealth == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(f"{p.parent}/hub-emergency-music.mp3")
                    pygame.mixer.music.play(loops = -1)
                self.canvas.delete("hp")
                self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20", tag = "hp")
                if self.critterHealth <= 0:
                    self.canvas.delete("all")
                    self.canvas.create_image(400, 400, image = self.bg_death)
                    self.canvas.create_text(400, 400, text = f"{self.yourCritterName} DIED", font = "Impact 30", fill = "red")
                    self.canvas.create_window(400, 600, window = self.restartGame)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(f"{p.parent}/funeral-music.mp3")
                    pygame.mixer.music.play(loops = -1)
                    internal_timer2.cancel()
                internal_timer2.start()
            ## Hunger goes down    
            elif randStat == 1:
                self.critterHun -= 1
                if self.critterHun == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(f"{p.parent}/hub-emergency-music.mp3")
                    pygame.mixer.music.play(loops = -1)
                self.canvas.delete("hgr")
                self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20", tag = "hgr")
                if self.critterHun <= 0:
                    self.canvas.delete("all")
                    self.canvas.create_image(400, 400, image = self.bg_death)
                    self.canvas.create_text(400, 400, text = f"{self.yourCritterName} DIED", font = "Impact 30", fill = "red")
                    self.canvas.create_window(400, 600, window = self.restartGame)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(f"{p.parent}/funeral-music.mp3")
                    pygame.mixer.music.play(loops = -1)
                    internal_timer2.cancel()
                internal_timer2.start()
            ## Love goes down    
            elif randStat == 2:
                self.critterLove -= 1
                ## Play emergency music if critter is about to die
                if self.critterLove == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(f"{p.parent}/hub-emergency-music.mp3")
                    pygame.mixer.music.play(loops = -1)
                self.canvas.delete("lov")
                self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20", tag = "lov")
                if self.critterLove <= 0:
                    self.canvas.delete("all")
                    self.canvas.create_image(400, 400, image = self.bg_death)
                    self.canvas.create_text(400, 400, text = f"{self.yourCritterName} DIED", font = "Impact 30", fill = "red")
                    self.canvas.create_window(400, 600, window = self.restartGame)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(f"{p.parent}/funeral-music.mp3")
                    pygame.mixer.music.play(loops = -1)
                    internal_timer2.cancel()
                internal_timer2.start()
        else:
            print("timer inactive")
            internal_timer2.start()

    def resetGame(self):
        pygame.mixer.music.stop()
        self.critterType = ""
        self.critterHealth = 3
        self.critterLove = 3
        self.critterHun = 3
        self.critterHealthMax = 4
        self.critterLoveMax = 4
        self.critterHunMax = 4
        self.yourCritterName = ""
        self.yourCritter = ""
        self.createCritter()

crittercraft()

