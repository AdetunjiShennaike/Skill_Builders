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

  if not(game.connected()):
    font = pygame.font.Sysfont('comicsans', 80)
    text = font.render('Waiting for an Opponent', 1, (255, 255, 255), True)
    surface.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
  else:
    font = pygame.font.Sysfont('comicsans', 60)
    text = font.render('Your Move', 1, (70, 190, 20))
    surface.blit(text, (80, 200))

    
    text = font.render('Opponent Move', 1, (70, 190, 20))
    surface.blit(text, (380, 200))

    p1move = game.player_move(0)
    p2move = game.player_move(1)

    if game.bothGo():
      text1 = font.render(p1move, 1, (0, 0, 0))
      text2 = font.render(p2move, 1, (0, 0, 0))


# a list for the buttons 
buttons = [Button('Rock', 50, 500, (200, 0, 0)), Button('Paper', 250, 500, (0, 180, 0)), Button('Scissor', 450, 500, (0, 0, 130))]

def main():
  # game  variables for the init game on
  gameInProgress = True
  clock = pygame.time.Clock()
  net = Network()
  player = int(net.getPos())
  print(f'You are Player {player}')

  while gameInProgress:
    clock.tick(60)
    # try to get a game/opponent
    try:
      game = net.send('get')
    except:
      gameInProgress = False
      print(f"Couldn't get game")
      break

    # if both player have gone redraw the window so that the text changes
    # then reset the game in the background while a delay is shown
    if game.bothGo():
      draw_window(win, game, player)
      pygame.time.delay(200)
      try:
        game = net.send('reset')
      except:
        gameInProgress = False
        print(f"Couldn't get game")
        break
      
      # display font based on if you won or lost 
      font = pygame.font.SysFont('comicsans', 40)
      if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
        text = font.render(f'Winner!', 1, (255, 255, 255))
      elif game.winner() == -1:
        text = font.render(f'Draw!', 1, (255, 255, 255))
      else:
        text = font.render(f'You Lose!', 1, (255, 255, 255))

      win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(2000)

    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()

      if e.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        for btn in buttons:
          if btn.click(pos) and game.connected():
            if player == 0:
              if not game.p1Go:
                net.send(btn.text)
            else:
              if not game.p2Go:
                net.send(btn.text)

  draw_window(win, game, player)

main()            
