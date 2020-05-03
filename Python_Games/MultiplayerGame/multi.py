import pygame

pygame.init()

# Global Variables
WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

clientNumber = 0

def draw_window():
  win.fill((255, 255, 255))
  pygame.display.update()

def main():
  gameInProgress = True

  while gameInProgress:
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()

      