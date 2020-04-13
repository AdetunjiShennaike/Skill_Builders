import math
import random
import pygame
import tkinter
from tkinter import messagebox

class cube(object):
  rows = 20
  w = 500
  def __init__(self, start, dirX=1,dirY=0, color=(0,255,0)):
    self.pos = start
    self.dirX = 1
    self.dirY = 0
    self.color = color

  def move(self, dirX, dirY):
    self.dirX = dirX
    self.dirY = dirY
    # Make it so that the snake is drawn at the current position
    self.pos = (self.pos[0] + self.dirX, self.pos[1] + self.dirY)

  def draw(self, surface, eyes=False):
    distance = self.w // self.rows
    # r = row and c = column
    r = self.pos[0]
    c = self.pos[1]
    # We remove 2 from distance to make sure that if we hit the edge of a screen we can still see where the snake is
    # Multiplying rows and columns by the distance + 1 so that it passes the gap of 2 
    pygame.draw.rect(surface, self.color, (r*distance + 1, c*distance + 1, distance - 2, distance - 2))
    if eyes:
      # Find the center and make the size of the eyes with radius
      center = distance // 2
      radius = 3
      # Make the actual circles of the snakes eyes
      circleMiddle = (r*distance + center - radius, c*distance + 8)
      circleMiddle2 = (r*distance + distance - radius*2, c*distance + 8)
      # Draw them 
      pygame.draw.circle(surface, (255,255,255), circleMiddle, radius)
      pygame.draw.circle(surface, (255,255,255), circleMiddle2, radius)

class snake(object):
  body = []
  turns = {}
  def __init__(self, color, pos):
    self.color = color
    # The front of the snake, this is what we use to turn
    self.head = cube(pos)
    # Add the head to the list, and make it the first entry
    self.body.append(self.head)
    # Use these to keep track of which direction we are heading, can't be moving on both simultaneously 
    self.dirX = 0
    self.dirY = 1

  def move(self):
    for e in pygame.event.get():
      # Quit the game
      if e.type == pygame.QUIT:
        pygame.quit()

      # Check if any keys were pressed at all
      # This method allows for diagonal movement and multipressed as opposed to checking individual key presses per loop
      keys = pygame.key.get_pressed()

      # The top left ofo the screen is (0,0) so to move left would be -1 and right would be 1, down 1 and up -1
      for key in keys:
        if keys[pygame.K_LEFT]:
          self.dirX = -1
          self.dirY = 0
          # add a new key-value pair to the dictionary and make the value the direction that was turned
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        elif keys[pygame.K_RIGHT]:
          self.dirX = 1
          self.dirY = 0
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        elif keys[pygame.K_UP]:
          self.dirX = 0
          self.dirY = -1
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        elif keys[pygame.K_DOWN]:
          self.dirX = 0
          self.dirY = 1
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

    # Moving the cubes at the same point as the snake head
    # i = iterator, c = cube, p = position
    for i, c in enumerate(self.body):
      p = c.pos[:]
      # If the current position exists in the turn dictionary, we want to move the current cube object 
      if p in self.turns:
        turn = self.turns[p]
        c.move(turn[0], turn[1])
        # If this is the last cube we will remove this movement from the list of turns so that it doesn't happen again unexpectedly
        if i == len(self.body) - 1:
          self.turns.pop(p)
      else:
        # Checking if we've hit the end of the screen, if we did we will move to the opposite side of the screen
        if c.dirX == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
        elif c.dirX == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
        elif c.dirY == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
        elif c.dirY == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
        else: c.move(c.dirX, c.dirY)

  def reset(self,pos):
    pass

  def addCube(self):
    # Defining the last part of the snake as the tail and making shorthand values for the x and y directions
    tail = self.body[-1]
    dx, dy = tail.dirX, tail.dirY
    
    # Depending on where the tail moves to we add a cube behind it in the appropriate direction
    if dx == 1 and dy == 0:
      self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
    elif dx == -1 and dy == 0:
      self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
    elif dx == 0 and dy == 1:
      self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
    elif dx == 0 and dy == -1:
      self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

    # Set new tail values for the snake
    self.body[-1].dirX = dx
    self.body[-1].dirY = dy

  
  def draw(self, surface):
    # i = iterator, c = cube Check if it is the head or not, if it is we add the eyes
    for i, c in enumerate(self.body):
      if i == 0:
        c.draw(surface, True)
      else:
        c.draw(surface)

def drawGrid(w, rows, surface):
  # The distance between the lines that are drawn
  sizeBetween = w // rows

  x = 0
  y = 0
  # for each row we will draw a line on the x and y axis ( 1 row, 1 colm)
  for i in range(rows):
    x = x + sizeBetween
    y = y + sizeBetween
    
    # Draw a vertical line starting at 0 y and going to to the width of the screen in a rgb color
    pygame.draw.line(surface, (255,255,255), (x,0) , (x,w))
    # Draw a horizontal line starting at 0 x and going to to the length of the screen in a rgb color
    pygame.draw.line(surface, (255,255,255), (0,y) , (w,y))
    # w for both since the length and width are the same size

def redrawWindow(surface):
  # Make the width and rows global to prevent having to pass them each call
  global width, rows, player, snack
  surface.fill((0,0,0))
  player.draw(surface)
  snack.draw(surface, True)
  drawGrid(width, rows, surface)
  pygame.display.update()

def randomSnack(rows,snack):
  positions = snack.body
  # Create food at a random point on the map
  while True:
    x = random.randrange(rows)
    y = random.randrange(rows)
    
    # We want to make sure that the food doesn't appear on top of the snake
    if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
      continue
    else:
      break

  return (x,y)

def message_box(subject, content):
  pass

def main():
  global width, rows, player, snack
  # The dimensions for the game window and the rows are for the game itself
  width = 500
  height = 500
  rows = 20
  window = pygame.display.set_mode((width, height))
  player = snake((0,255,0), (10,10))
  snack = cube(randomSnack(rows, player), color=(220,220,220))

  # Session indicates if the game is happening at the moment or not
  inSession = True

  # Generate a built in clock from pygame
  clock = pygame.time.Clock()

  # Start the game loop
  while inSession:
    pygame.time.delay(50)
    clock.tick(10) # Makes the game run at x frames per second

    # Move the snake accross the screen
    player.move()
    # If the snake head touches the food we add onto the snack and spawn more food
    if player.body[0].pos == snack.pos:
      player.addCube()
      snack = cube(randomSnack(rows, player), color=(220,220,220))
    redrawWindow(window)

main()