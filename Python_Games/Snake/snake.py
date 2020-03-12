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
  pass

def randomSnack(rows,items):
  pass

def message_box(subject, content):
  pass

def main():
  width = 500
  height = 500
  rows = 20
  window = pygame.display.set_mode((width, height))
  player = snake((0,255,0), (10,10))
  inSession = True
  while inSession:
    pygame.time.delay