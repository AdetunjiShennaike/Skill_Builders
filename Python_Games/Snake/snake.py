import math
import random
import pygame
import tkinter
from tkinter import messagebox

class cube(object):
  def __init__(self, start, dirnx=1,dirny=0, color(255,0,0)):
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
  pass

def redrawWindow(surface):
  # Make the width and rows global to prevent having to pass them each call
  global width, rows
  window.fill((255,255,255))
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

    redrawWindow(window, width, rows)