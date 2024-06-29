import sys
import pygame
import numpy as np


pygame.init()




# Colors that will be used for board, token, etc
WHITE = (255,255,255)
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