import pygame


class Player():
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    # Shorten the draw process by making this a variable
    self.rect = (x, y, width, height)
    # Constant velocity/movement speed of the player
    self.vel = 5

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
