from tkinter import * # Import tkinter
    
class Testing:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Test") # Set a title

        frame = Frame(window) # Create and add a frame to window
        frame.pack()
        btCare = Button(frame, text = "Care", 
            command = self.care)
        btCare.grid(row = 1, column = 1)
        btPlay = Button(frame, text = "Play", 
            command = self.play)
        btPlay.grid(row = 1, column = 2)
        
        window.mainloop() # Create an event loop

    def care(self):
        print("check button is " 
            + ("checked " if self.v1.get() == 1 else "unchecked"))
        
    def play(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") 
            + " is selected " )

Testing() # Create GUI