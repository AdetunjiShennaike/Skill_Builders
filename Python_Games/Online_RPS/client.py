import pygame
import pickle
from network import Network

# initialize the pygame library
pygame.init()

# global variables 
WIDTH = 700
HEIGHT = 700
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("RPS")

class Button:
  def __init__(self, text, x, y, color):
    self.text = text
    self.x = x
    self.y = y
    self.color = color
    self.width = 150
    self.height = 100

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    font = pygame.font.SysFont('comicsans', 40)
    text = font.render(self.text, 1, (255, 255, 255))
    # math to center the text with both heigh and width based on how long the text input is
    surface.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
  
  # checking where we click on the screen, for the rock paper and scissors buttons
  def click(self, pos):
    x1 = pos[0]
    y1 = pos[1]
    # check if the coordinates of the mouse is within the box for the button
    if self.x <= x1 <= self.width and self.y <= y1 <= self.y + self.height:
      return True
    else:
      return False

def draw_window(surface, game, player):
  surface.fill((128, 128, 128))


def main():
  pass

main()            
