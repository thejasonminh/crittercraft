from tkinter import * # Import tkinter

# Author: Jason Ngo, Jayden Jung, Jueun Kang
# Class: INF 0452H; Information Design Studio V: Coding
# Instructor: Maher Elshakankiri
# Assignment: Final Project
# Date Created: 11/25/2023
# Last Modified: 11/25/2023
# Purpose: CritterCraft

from tkinter import * # Import tkinter
from pathlib import Path 
from tkinter import messagebox
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
        self.critterHealth = 2
        self.critterLove = 2
        self.critterHun = 2
        self.critterHealthMax = 3
        self.critterLoveMax = 3
        self.critterHunMax = 3
        self.yourCritterName = ""
        self.yourCritter = ""
        
        # Initiliazing game mode status
        self.gamemode = False

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
        
        ## Add button to the canvas
        self.canvas.create_window(400, 600, window = self.btn_next)

        ## Make buttons to Care or Play with pet
        self.btn_care = Button(self.window, text = "Care", font = self.critterFont, bg = "#8cc45c", command = self.careWindow)
        self.btn_play = Button(self.window, text = "Play", font = self.critterFont, bg = "#8cc45c", command = self.playWindow)

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
        # Internal timer to kill the critter
        threading.Timer(5.0, self.hubTimer).start()

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

    def careWindow(self):
        careWindow = Toplevel(self.window)
        careWindow.title("Care")
        careWindow.geometry("200x100")
        framegames = Frame(careWindow) # Create and add a frame to window
        framegames.pack()
        btHealth = Button(framegames, text = "Clean", command=self.care(1))
        btHealth.grid(row = 1, column = 1)
        btHunger = Button(framegames, text = "Feed", command=self.care(2))
        btHunger.grid(row = 2, column = 1)
        btLove = Button(framegames, text = "Cuddle", command=self.care(3))
        btLove.grid(row = 3, column = 1)

    def care(self, num):
        if num == 1:
            if self.critterHealth < self.critterHealthMax:
                self.critterHealth += 1
                self.canvas.delete("hp")
                self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20", tag = "hp")
            else:
                None
        if num == 2: 
            if self.critterHun < self.critterHunMax:
                self.critterHun += 1
                self.canvas.delete("hgr")
                self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20", tag = "hgr")
            else:
                None
        if num == 3:
            if self.critterLove < self.critterLoveMax:
                self.critterLove += 1
                self.canvas.delete("lov")
                self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20", tag = "lov")
            else:
                None
        rando = random.randint(0,4)
        if rando == 1:
            print(1)
            threading.Timer(10.0, self.hubTimer).start()

    def playWindow(self):
        gameswindow = Toplevel(self.window)
        gameswindow.title("Play")
        gameswindow.geometry("200x100")
        framegames = Frame(gameswindow) # Create and add a frame to window
        framegames.pack()
        btMem = Button(framegames, text = "Memorize Me!", command = self.memGame)
        btMem.grid(row = 1, column = 1)
        btTic = Button(framegames, text = "Tic Tac Bone!", 
            command = self.ticGame)
        btTic.grid(row = 2, column = 1)
        btGuess = Button(framegames, text = "Guess the love!", 
            command = self.guessGame)
        btGuess.grid(row = 3, column = 1)
    
    # def memGame(self):
    #     self.gamemode = True
    #     outcome = 0
    #     print(outcome)
    #     class MemorizationGame:
    #         def __init__(self):
    #             self.master = Tk()
    #             self.master.title("Memorization Game")

    #             # Initialize sequences
    #             self.sequence = []
    #             self.player_sequence = []

    #             self.critterfont = font.Font(family = "Helvetica")
    #             self.critterFont = font.Font(size = 20)
                
    #             # Create labels
    #             label_frame = Frame(self.master)
    #             label_frame.pack(pady=10)

    #             self.lbWelcome = Label(label_frame, text="Welcome to Memorize Me!").grid(row=0, column=1)
    #             self.lbInstructions = Label(label_frame, text="Press start to see the pattern, memorize and copy it, and click submit.").grid(row=1, column=1)
    #             self.statusVar = StringVar()
    #             self.statusVar.set("Press start!")
    #             self.lbStatus = Label(label_frame, textvariable = self.statusVar, fg = 'blue').grid(row=3, column=1)

    #             # Create buttons
    #             button_frame = Frame(self.master)
    #             button_frame.pack(pady=10)

    #             # Up and Down buttons
    #             self.btUp = Button(button_frame, text="Up", command=lambda: self.add_to_player_sequence("Up"))
    #             self.btUp.grid(row=0, column=1, pady=5)
    #             self.btUp['font'] = self.critterfont

    #             self.btDown = Button(button_frame, text="Down", command=lambda: self.add_to_player_sequence("Down"))
    #             self.btDown.grid(row=2, column=1, pady=5)
    #             self.btDown['font'] = self.critterfont

    #             # Left and Right buttons
    #             self.btLeft = Button(button_frame, text="Left", command=lambda: self.add_to_player_sequence("Left"))
    #             self.btLeft.grid(row=1, column=0, padx=5)
    #             self.btLeft['font'] = self.critterfont

    #             self.btRight = Button(button_frame, text="Right", command=lambda: self.add_to_player_sequence("Right"))
    #             self.btRight.grid(row=1, column=2, padx=5)
    #             self.btRight['font'] = self.critterfont

    #             # Start and Submit buttons
    #             start_button = Button(button_frame, text="Start", command=self.start_game)
    #             start_button.grid(row=1, column=1, pady=10)
    #             start_button['font'] = self.critterfont

    #             submit_button = Button(button_frame, text="Submit Sequence", command=self.check_sequence)
    #             submit_button.grid(row=3, column=1)
    #             submit_button['font'] = self.critterfont

    #             # Disable buttons initially
    #             self.disable_buttons()
    #             self.master.mainloop()

    #         def disable_buttons(self):
    #             for direction in ["Left", "Right", "Up", "Down"]:
    #                 self.get_button(direction).config(state=DISABLED)

    #         def enable_buttons(self):
    #             for direction in ["Left", "Right", "Up", "Down"]:
    #                 self.get_button(direction).config(state=NORMAL)

    #         def add_to_player_sequence(self, direction):
    #             self.player_sequence.append(direction)

    #         def start_game(self):
    #             self.statusVar.set("Wait and watch... When the pattern finishes, repeat it, and press submit!")
    #             self.sequence = []
    #             self.player_sequence = []
    #             self.disable_buttons()
    #             self.generate_sequence()
    #             self.show_sequence()
    #             self.enable_buttons()

    #         def generate_sequence(self):
    #             directions = ["Left", "Right", "Up", "Down"]
    #             for i in range(5):  # Adjust the number of moves in the sequence as needed
    #                 self.sequence.append(random.choice(directions))

    #         def show_sequence(self):
    #             for i, direction in enumerate(self.sequence):
    #                 self.master.after(i * 1500, lambda d=direction: self.highlight_button(d))
    #                 self.master.after((i + 1) * 1800, self.clear_highlight)

    #         def highlight_button(self, direction):
    #             self.get_button(direction).config(fg="red")

    #         def clear_highlight(self):
    #             for direction in ["Left", "Right", "Up", "Down"]:
    #                 self.get_button(direction).config(fg="black")

    #         def check_sequence(self):
    #             if self.player_sequence == self.sequence:
    #                 messagebox.showinfo("Success", "Correct sequence! You won!")
    #                 print(3)
    #                 outcome = 1
    #                 print(f"Game won. Outcome points: {outcome}")
    #                 self.master.destroy()
    #             else:
    #                 messagebox.showerror("Error", "Incorrect sequence. Try again.")
    #                 self.master.destroy()
    #             self.statusVar.set("Press start!")
    #             self.disable_buttons()
    #             self.sequence = []
    #             self.player_sequence = []

    #         def get_button(self, direction):
    #             if direction == "Up":
    #                 return self.btUp
    #             elif direction == "Down":
    #                 return self.btDown
    #             elif direction == "Left":
    #                 return self.btLeft
    #             elif direction == "Right":
    #                 return self.btRight

    #     MemorizationGame()
        
    #     print(f"Game done playing. Outcome: {outcome}")
    #     self.gamemode = False
    #     threading.Timer(5.0, self.hubTimer).start()

    def ticGame(self):
        # inc hunger
        print(5)

    def guessGame(self):
        # inc love
        print(6)
    
    # Method that rolls random events designated to lower stats and kill the critter
    def hubTimer(self):
        randStat = random.randint(0, 3)
        print("timer tick")
        ## Health goes down
        if randStat == 0:
            self.critterHealth -= 1
            self.canvas.delete("hp")
            self.canvas.create_text(200, 100, text = f"Health: {self.critterHealth} / {self.critterHealthMax}", font = "Helvetica 20", tag = "hp")
            if self.critterHealth <= 0:
                self.canvas.delete("all")
                self.canvas.create_image(400, 400, image = self.bg_death)
                self.canvas.create_text(400, 400, text = "YOU DIED", font = "Impact 30", fill = "red")
                time.sleep(5)
                self.window.destroy()
                #sys.exit(0)
            threading.Timer(5.0, self.hubTimer).start()
        ## Hunger goes down    
        elif randStat == 1:
            self.critterHun -= 1
            self.canvas.delete("hgr")
            self.canvas.create_text(400, 100, text = f"Hunger: {self.critterHun} / {self.critterHunMax}", font = "Helvetica 20", tag = "hgr")
            if self.critterHun <= 0:
                self.canvas.delete("all")
                self.canvas.create_image(400, 400, image = self.bg_death)
                self.canvas.create_text(400, 400, text = "YOU DIED", font = "Impact 30", fill = "red")
                time.sleep(5)
                self.window.destroy()
                #sys.exit(0)
            threading.Timer(5.0, self.hubTimer).start()
        ## Love goes down    
        elif randStat == 2:
            self.critterLove -= 1
            self.canvas.delete("lov")
            self.canvas.create_text(600, 100, text = f"Love: {self.critterLove} / {self.critterLoveMax}", font = "Helvetica 20", tag = "lov")
            if self.critterLove <= 0:
                self.canvas.delete("all")
                self.canvas.create_image(400, 400, image = self.bg_death)
                self.canvas.create_text(400, 400, text = "YOU DIED", font = "Impact 30", fill = "red")
                time.sleep(5)
                self.window.destroy()
                #sys.exit(0)
            threading.Timer(5.0, self.hubTimer).start()

crittercraft()