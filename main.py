from tkinter import *
import random

##Snake Game by Wazingwa Mugala

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    pass

class Food:
    pass


def next_turn():
    pass



def change_direction():
    pass

def check_collisions():
    pass

def change_direction(new_direction):
    pass

def game_over():
    pass


window = Tk()
window.title("Snago by SWE. Wazingwa")
window.resizable(False,False)

score = 0
direction = "down"


label = Label(window, text="Score:{}". format(score), font=("consolas", 20))
label.pack()


canvas = Canvas(window, bg=BACKGROUND_COLOR, height= GAME_HEIGHT, width=GAME_WIDTH)

canvas.pack()


window.update()
window_width = window.winfo_width()
window_height
window.mainloop()