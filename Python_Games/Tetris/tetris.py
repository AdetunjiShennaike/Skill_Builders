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
Y_AXIS = (HEIGHT - PLAY_HEIGHT) / 2

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

def draw_grid(surface, grid):
  # Draw the lines of the grid for the play area
  for i in range(len(grid)):
    pygame.draw.line(surface, (128, 128, 128), (X_AXIS, Y_AXIS + (i * BLOCK_SIZE)), (X_AXIS + PLAY_WIDTH, Y_AXIS + (i * BLOCK_SIZE)))
    for j in range(len(grid[i])):
      pygame.draw.line(surface, (128, 128, 128), (X_AXIS + (j * BLOCK_SIZE), Y_AXIS), (X_AXIS + (j * BLOCK_SIZE), Y_AXIS + PLAY_HEIGHT))

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
  # Give us a random shape
  return Piece(5, 0, random.choice(shapes))

def middle_text():
  # 
  pass

def clear_rows():
  # 
  pass

def next_shape():
  # 
  pass

def draw_window(surface, grid):
  # Setting up the overall game area
  surface.fill((0, 0, 0))

  # Creating the title and centering it to the top
  pygame.font.init()
  font = pygame.font.SysFont('comicsans', 60)
  label = font.render('Tetris', 1, (255, 255, 255))
  # Blit to write and then 2nd input is Centering
  surface.blit(label, (X_AXIS + (PLAY_WIDTH / 2) - (label.get_width() / 2), 30))

  # For each individual square on the game space we draw the 
  # corresponding color based on the create grid fn
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      pygame.draw.rect(surface, grid[i][j], (X_AXIS + (j * BLOCK_SIZE), Y_AXIS + (i * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE), 0)

  # Border for the play area
  pygame.draw.rect(surface, (255, 0, 0), (X_AXIS, Y_AXIS, PLAY_WIDTH, PLAY_HEIGHT), 4)

  # Draw the grid
  draw_grid(surface, grid)
  pygame.display.update()


def main(surface):
  # Set up the initial game variables
  locked_pos = {}
  grid = create_grid(locked_pos)

  change_shape = False
  gameInProgress = True
  current_shape = get_shape()
  next_shape = get_shape()
  clock = pygame.time.Clock()
  fall_time = 0

  while gameInProgress:
    for e in pygame.event.get():
      if e.type = pygame.QUIT:
        pygame.quit()
      
      if e.type = pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
          current_shape.x -= 1
          if not valid_space(current_shape, grid):
            current_shape.x += 1
        if e.key == pygame.K_RIGHT:
          current_shape.x += 1
          if not valid_space(current_shape, grid):
            current_shape.x -= 1
        if e.key == pygame.K_UP:
          current_shape.rotation += 1
          if not valid_space(current_shape, grid):
            current_shape.rotation -= 1
        if e.key == pygame.K_DOWN:
          current_shape.y += 1
          if not valid_space(current_shape, grid):
            current_shape.y -= 1

  draw_window(surface, grid)


def main_menu(win):
  # 
  main(win)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')
main_menu(win)