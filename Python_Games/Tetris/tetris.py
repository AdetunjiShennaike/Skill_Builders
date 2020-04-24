import pygame
import random

# Global Variables
# Screen size
WIDTH = 800
HEIGHT = 700
# Game area size, Tetris is a 10x20 grid
PLAY_WIDTH = 300 # 300 / 10 = 30
PLAY_HEIGHT = 600 # 600 / 20 = 30
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

class Piece(object):
  # Create the piece that should be rendered with the correct color and start location
  # Adding the rotation value for the shape to change
  def __init__(self, x, y, shape):
    self.x = x
    self.y = y
    self.shape = shape
    self.color = shape_colors[shapes.index(shape)]
    self.rotation = 0

def create_grid(locked_pos = {}):
  # Create the grid as it is at that moment of the game
  # Create a list of color values for every iteration in another list called grid
  grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

  # Check if the current stage grid already has tetrominos in it and 
  # if it does then assign that color to the spot on the grid
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if(j, i) in locked_pos:
        grid[i][j] = locked_pos[(j, i)]
  return grid

def draw_grid():
  # 
  pass

def convert_shape():
  # 
  pass

def valid_space():
  # 
  pass

def game_lost():
  # 
  pass

def get_shape():
  # 
  pass

def middle_text():
  # 
  pass

def clear_rows():
  # 
  pass

def next_shape():
  # 
  pass

def draw_window():
  # 
  pass

def main():
  # 
  pass

def main_menu():
  # 
  pass

main_menu()