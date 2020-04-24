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

class Piece(object):
  # 
  pass

def create_grid():
  # 
  pass

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