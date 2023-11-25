import tkinter as tk
import random

class CatchTheLoveGame:
    def __init__(self):
        self.love = 0  # Initial love level
        self.love_cap = 10  # Maximum love level

        self.window = tk.Tk()
        self.window.title("Catch the Love")

        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="white")
        self.canvas.pack()

        self.basket = self.canvas.create_rectangle(150, 350, 250, 370, fill="blue")
        self.canvas.bind("<Left>", lambda event: self.move_basket(-20, 0))
        self.canvas.bind("<Right>", lambda event: self.move_basket(20, 0))

        self.falling_love = []

        self.update_love_display()
        self.spawn_love()

        self.window.mainloop()

    def move_basket(self, dx, dy):
        basket_coords = self.canvas.coords(self.basket)
        if 0 < basket_coords[0] + dx < 400 and 0 < basket_coords[2] + dx < 400:
            self.canvas.move(self.basket, dx, dy)

    def spawn_love(self):
        x = random.randint(50, 350)
        y = 0
        love_shape = self.canvas.create_text(x, y, text="❤", font=("Helvetica", 12), fill="red")
        self.falling_love.append(love_shape)
        self.move_love(love_shape)

    def move_love(self, love_shape):
        if self.canvas.coords(love_shape)[1] < 400:
            self.canvas.move(love_shape, 0, 5)
            self.window.after(50, lambda: self.move_love(love_shape))
        else:
            self.check_catch(love_shape)

    def check_catch(self, love_shape):
        basket_coords = self.canvas.coords(self.basket)
        love_coords = self.canvas.coords(love_shape)

        if (
            basket_coords[0] < love_coords[0] < basket_coords[2]
            or basket_coords[0] < love_coords[2] < basket_coords[2]
        ):
            self.love += 1
            self.update_love_display()
            self.falling_love.remove(love_shape)
            self.canvas.delete(love_shape)
            self.spawn_love()

    def update_love_display(self):
        self.canvas.delete("love_display")
        love_display = f"Love Level: {self.love}/{self.love_cap}"
        self.canvas.create_text(200, 20, text=love_display, font=("Helvetica", 12), tags="love_display")

if __name__ == "__main__":
    catch_the_love_game = CatchTheLoveGame()
