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
  def __init__(self, color, pos):
    pass

  def move(self):
    pass

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