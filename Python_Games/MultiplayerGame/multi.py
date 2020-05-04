import pygame

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
    self.rect = (x, y, width, height)

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)
  
  def move(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
      self.x -= self.vel
      
    if keys[pygame.K_RIGHT]:
      self.x += self.vel

    if keys[pygame.K_UP]:
      self.y -= self.vel

    if keys[pygame.K_DOWN]:
      self.y += self.vel


def draw_window(surface):
  surface.fill((255, 255, 255))
  pygame.display.update()

def main():
  gameInProgress = True

  while gameInProgress:
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()

    draw_window(win)