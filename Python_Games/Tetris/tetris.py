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
X_AXIS = int((WIDTH - PLAY_WIDTH) / 2)
Y_AXIS = int(HEIGHT - PLAY_HEIGHT)

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
        color = locked_pos[(j, i)]
        grid[i][j] = color
  
  return grid

def draw_grid(surface, grid):
  # For each individual square on the game space we draw the 
  # corresponding color based on the create grid fn
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      pygame.draw.rect(surface, grid[i][j], (X_AXIS + (j * BLOCK_SIZE), Y_AXIS + (i * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE), 0)

  # Draw the lines of the grid for the play area
  for i in range(len(grid)):
    pygame.draw.line(surface, (128, 128, 128), (X_AXIS, Y_AXIS + (i * BLOCK_SIZE)), (X_AXIS + PLAY_WIDTH, Y_AXIS + (i * BLOCK_SIZE)))
    for j in range(len(grid[i])):
      pygame.draw.line(surface, (128, 128, 128), (X_AXIS + (j * BLOCK_SIZE), Y_AXIS), (X_AXIS + (j * BLOCK_SIZE), Y_AXIS + PLAY_HEIGHT))

def convert_shape(shape):
  # Convert the shape that was drawn with periods and zeros to a position the computer can read and generate/render
  pos = []
  # Take the remainder between the currently selected and the max number of shape rotations
  # This gives you an individual list within the shape list
  form = shape.shape[shape.rotation % len(shape.shape)]

  # Start the conversion of the grabbed form
  for i, line in enumerate(form):
    # Change each section to a list to span through each individual point
    sect = list(line)
    for j, point in enumerate(sect):
      if point == '0':
        # Marks the x and y cordinate of the 0 using the section it was found in 
        # and the point/column, it was located within that section
        pos.append((shape.x + j, shape.y + i))

  # Off set the x and y values to move them up and left inside of their form
  # this for most of the forms accurately removes the counting of the periods in x and y values
  # the -4 makes sure that the shape is spawned above the game area 
  for i, spot in enumerate(pos):
    pos[i] = (spot[0] - 2, spot[1] - 4)

  return pos

def valid_space(shape, grid):
  # Grab all of the positions of the game space, only if the position is the color black - meaning its empty
  accepted = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
  # Flatten the list to just a list of tuples instead of a list of lists of tuples
  # s = spot/coordinate, For each list in the accepted list we will make a tuple
  accepted = [s for subList in accepted for s in subList]

  # Convert the shape and store its current location
  formed = convert_shape(shape)

  # Check if the given position is within the game window or not
  for pos in formed:
    if pos not in accepted:
      # We only check if the y value has passed the game window
      if pos[1] > -1:
        return False
  
  return True

def game_lost(pos):
  # Check if any pieces/shapes are at the top of the screen(above it)
  for spot in pos:
    x, y = spot
    if y < 1:
      return True
  
  return False

def get_shape():
  # Give us a random shape 
  return Piece(5, 0, random.choice(shapes))
  
def middle_text(surface, text, size, color):
  # 
  font = pygame.font.SysFont('comicsans', size, bold=True)
  label = font.render(text, 1, color)

  surface.blit(label, (X_AXIS + int(PLAY_WIDTH / 2) - int(label.get_width() / 2), Y_AXIS + int(PLAY_HEIGHT / 2) - int(label.get_height() / 2)))

def clear_rows(grid, locked):
  # Erase blocks when a row gets filled up 
  inc = 0
  # loop through the y axis backwards
  for i in range(len(grid)-1, -1, -1):
    row = grid[i]
    # if none of the spots are black that means theres a piece of a shape in the entire row
    if (0, 0, 0) not in row:
      # Add to the increment and set the index
      inc += 1
      index = i
      for j in range(len(row)):
        # Try and delete all of the locked positions from the dict so that the colors are gone as well
        try:
          del locked[(j, i)]
        except:
          continue

    if inc > 0:
      # Use lambda to sort the key/list by the Y values, as per the use of x[1] 
      for key in sorted(list(locked), key = lambda x:x[1])[::-1]:
        x, y = key
        # Move anything above the indexed row down, anything below it will remian the same
        if y < index:
          # Use the increment to shift down appropriately based on which rows were deleted 
          newKey = (x, y + inc)
          # Switched the new spot to the previous spots color, while simultaneously removing it from the dictionary
          locked[newKey] = locked.pop(key)

  return inc

def draw_next_shape(shape, surface):
  # The text to go above the next shape window 
  font = pygame.font.SysFont('comicsans', 20)
  label = font.render(f'Next Shape', 1, (255, 255, 255))

  # Starting points of the container 
  startX = X_AXIS + int(PLAY_WIDTH * 1.25)
  startY = Y_AXIS + int(PLAY_HEIGHT / 3)

  form = shape.shape[shape.rotation % len(shape.shape)]

  for i, line in enumerate(form):
    sect = list(line)
    for j, spot in enumerate(sect):
      if spot == '0':
        pygame.draw.rect(surface, shape.color, (startX + (j * BLOCK_SIZE), startY + (i * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE), 0)

  surface.blit(label, (startX + 40, startY - 35))

def draw_window(surface, grid, score=0):
  # Setting up the overall game area
  surface.fill((0, 0, 0))

  # Creating the title and centering it to the top
  pygame.font.init()
  font = pygame.font.SysFont('comicsans', 60)
  label = font.render('Tetris', 1, (255, 255, 255))
  # Blit to write and then 2nd input is Centering
  surface.blit(label, (X_AXIS + int(PLAY_WIDTH / 2) - int(label.get_width() / 2), 30))

  # The text to go below the next shape window 
  scoreFont = pygame.font.SysFont('comicsans', 20)
  scoreText = scoreFont.render(f'Score: {score}', 1, (255, 255, 255))

  # Starting points of the container 
  startX = X_AXIS + int(PLAY_WIDTH * 1.25)
  startY = Y_AXIS + int(PLAY_HEIGHT / 3)
  
  # Blit for the score text
  surface.blit(scoreText, (startX + 45, startY + 130))

  # Border for the play area
  pygame.draw.rect(surface, (255, 0, 0), (X_AXIS, Y_AXIS, PLAY_WIDTH, PLAY_HEIGHT), 4)

  # Draw the grid
  draw_grid(surface, grid)


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
  fall_speed = 0.27
  level_time = 0
  score = 0

  while gameInProgress:
    # Update the grid once a shape is placed and a new one is given
    grid = create_grid(locked_pos)
    fall_time += clock.get_rawtime()
    level_time += clock.get_rawtime()
    # Grab the amount of time it took for the shape to fall to the bottom of the screen/ the while loop runtime 
    clock.tick()

    # Increase the fall speed over time
    if level_time/1000 > 5:
      level_time = 0
      if fall_speed > .12:
        fall_speed -= .005

    # When the fall time passes the fall speed we reset it to 0 and speed up the current shape 
    if fall_time/1000 > fall_speed:
      fall_time = 0
      current_shape.y += 1
      if not(valid_space(current_shape, grid)) and current_shape.y > 0:
        current_shape.y -= 1
        change_shape = True 

    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()
      
      if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
          current_shape.x -= 1
          if not(valid_space(current_shape, grid)):
            current_shape.x += 1
        if e.key == pygame.K_RIGHT:
          current_shape.x += 1
          if not(valid_space(current_shape, grid)):
            current_shape.x -= 1
        if e.key == pygame.K_UP:
          current_shape.rotation += 1
          if not(valid_space(current_shape, grid)):
            current_shape.rotation -= 1
        if e.key == pygame.K_DOWN:
          current_shape.y += 1
          if not(valid_space(current_shape, grid)):
            current_shape.y -= 1

    # Grab the position of the current shape
    shape_pos = convert_shape(current_shape)
    # Grab the different positions of the shape and add the color to it, so that it can be drawn
    for i in range(len(shape_pos)):
      x, y = shape_pos[i]
      if y > -1:
        grid[y][x] = current_shape.color

    # Once we have hit another shape or the floor we will add the current shape to the dictionary 
    # locked pos to have the colors show up when calling create grid
    if change_shape:
      for spot in shape_pos:
        p = (spot[0], spot[1])
        locked_pos[p] = current_shape.color
      # Switch the shape to the next one
      current_shape = next_shape
      next_shape = get_shape()
      change_shape = False
      multiplier = clear_rows(grid, locked_pos)
      score += multiplier * 100 


    draw_window(surface, grid, score)
    draw_next_shape(next_shape, surface)

    pygame.display.update()

    if game_lost(locked_pos):
      middle_text(surface, "You Lost!", 80, (255, 255, 255)
      pygame.time.wait(5000)
      gameInProgress = False


def main_menu(win):
  # 
  main(win)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')
main_menu(win)