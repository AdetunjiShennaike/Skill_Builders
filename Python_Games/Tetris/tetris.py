import pygame
import random

# Global Variables
# Screen size
WIDTH = 800
HEIGHT = 700
# Game area size
PLAY_WIDTH = 300
PLAY_HEIGHT = 600
BLOCK_SIZE = 30
# Game area starting points
X_AXIS = (WIDTH - PLAY_WIDTH) / 2
Y_AXIS = (HEIGHT - PLAY_HEIGHT) /2

# Shapes
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
      ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
      ['.....',
      '...0.',
      '..00.',
      '..0..',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
      ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
      ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
      ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
      ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
      ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
# Shape lists colors and shapes have matching indices
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (25, 265, 0), (0, 0, 255), (128, 0, 128)]