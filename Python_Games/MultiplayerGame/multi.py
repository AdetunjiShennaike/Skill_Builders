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

    self.update()

  def update(self):
    # After a movement is done update the rect so that the display is updated
    self.rect = (self.x, self.y, self.width, self.height)


def read_position(str):
  # Read the position that is being sent from the network as a string and
  # return a usbale tuple
  str = str.split(',')
  return int(str[0]), int(str[1])

def make_position(tupl):
  # Take in a tuple and turn it into a string that can be sent over the network
  return str(f"{tupl[0]},{tupl[1]}")

def draw_window(surface, pOne, pTwo):
  # Creating the game window and player
  surface.fill((255, 255, 255))
  pOne.draw(surface)
  pTwo.draw(surface)
  pygame.display.update()

def main(surface):
  # Set up the starting game logic
  gameInProgress = True
  net = Network()
  # Return the starting positions of the characters
  startPos = read_position(net.getPos())
  playerOne = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
  playerTwo = Player(0, 0, 100, 100, (0, 255, 0))
  clock = pygame.time.Clock()

  while gameInProgress:
    clock.tick(60)

    p2Pos = read_position(net.send(make_position((playerOne.x, playerOne.y))))
    playerTwo.x = p2Pos[0]
    playerTwo.y = p2Pos[1]
    playerTwo.update()

    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()

    playerOne.move()
    draw_window(surface, playerOne, playerTwo)


main(win)