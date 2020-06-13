import pygame
from network import Network
from player import Player

pygame.init()

# Global Variables
WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")


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
  pOne = net.getPos()

  clock = pygame.time.Clock()

  while gameInProgress:
    clock.tick(60)
    pTwo = net.send(pOne)

    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()

    playerOne.move()
    draw_window(surface, playerOne, playerTwo)


main(win)