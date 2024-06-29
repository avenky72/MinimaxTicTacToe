import sys
import pygame
import tkinter as tk
import numpy as np





# Colors that will be used for board, token, etc
WHITE = rgb(255,255,255)
GRAY = (180,180,180)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)


# Size of game screen, board, tokens
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RAD = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
cells = 200
canvas_width = cells * BOARD_COLS
canvas_height = cells * BOARD_ROWS

root = tk.Tk()
root.title("Tic Tac Toe MiniMax AI")

#BOARD = np.zeros((BOARD_ROWS, BOARD_COLS))

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
        
def draw_board(color):
    for i in range(1, BOARD_ROWS):
        canvas.create_line(0, i * cells, canvas_width, i * cells, fill=color, width=LINE_WIDTH)
    
    for j in range(1, BOARD_COLS):
        canvas.create_line(j * cells, 0, j * cells, canvas_height, fill=color, width=LINE_WIDTH)
draw_board(GREEN)

root.mainloop()