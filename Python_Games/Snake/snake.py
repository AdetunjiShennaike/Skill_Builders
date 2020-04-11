import math
import random
import pygame
import tkinter
from tkinter import messagebox

class cube(object):
  def __init__(self, start, dirnx=1,dirny=0, color=(255,0,0)):
    pass

  def move(self, dirnx, dirny):
    pass

  def draw(self, sureface, eyes=False):
    pass

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
        if key[pygame.K_LEFT]:
          self.dirX = -1
          self.dirY = 0
          # add a new key-value pair to the dictionary and make the value the direction that was turned
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        elif key[pygame.K_RIGHT]:
          self.dirX = 1
          self.dirY = 0
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        elif key[pygame.K_UP]:
          self.dirX = 0
          self.dirY = -1
          self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        elif key[pygame.K_DOWN]:
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
        if i == len(self.body)-1:
          self.turns.pop(p)
      else:
        

  def reset(self,pos):
    pass

  def addCube(self):
    pass
  
  def draw(self, surface):
    pass

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
  global width, rows
  surface.fill((255,255,255))
  drawGrid(width, rows, surface)
  pygame.display.update()

def randomSnack(rows,items):
  pass

def message_box(subject, content):
  pass

def main():
  global width, rows
  # The dimensions for the game window and the rows are for the game itself
  width = 500
  height = 500
  rows = 20
  window = pygame.display.set_mode((width, height))
  player = snake((0,255,0), (10,10))

  # Session indicates if the game is happening at the moment or not
  inSession = True

  # Generate a built in clock from pygame
  clock = pygame.time.Clock()

  # Start the game loop
  while inSession:
    pygame.time.delay(50)
    clock.tick(10) # Makes the game run at x frames per second

    redrawWindow(window)

main()