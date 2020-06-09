import pygame
from network import Network

pygame.init()

# Global Variables
WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    # Shorten the draw process by making this a variable
    self.rect = (x, y, width, height)

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)
  
  def move(self):
    # Check which keys were pressed and I'm using only if 
    # statements so that diagonal movement is allow
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
      self.x -= self.vel
      
    if keys[pygame.K_RIGHT]:
      self.x += self.vel

    if keys[pygame.K_UP]:
      self.y -= self.vel

    if keys[pygame.K_DOWN]:
      self.y += self.vel

    # After a movement is done update the rect so that the display is updated
    self.rect = (self.x, self.y, self.width, self.height)


def read_position(str):
  str = str.split(',')
  return int(str[0]), int(str[1])

def make_position(tupl):
  return str(f"{tupl[0]},{tupl[1]}")


def draw_window(surface, player):
  # Creating the game window and player
  surface.fill((255, 255, 255))
  player.draw(surface)
  pygame.display.update()

def main(surface):
  # Set up the starting game logic
  gameInProgress = True
  net = Network()
  # Return the starting positions of the characters
  startPos = net.getPos()
  playerOne = Player(50, 50, 100, 100, (0, 255, 0))
  clock = pygame.time.Clock()

  while gameInProgress:
    clock.tick(60)
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()

    playerOne.move()
    draw_window(surface)


main(win)