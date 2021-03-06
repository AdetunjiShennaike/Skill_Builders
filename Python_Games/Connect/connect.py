import numpy
import pygame
import math

# Board dimensions
WIDTH = 7
HEIGHT = 6
CONNECT = 4
# Dynamic
# WIDTH = int(input(f'How many columns?'))
# HEIGHT = int(input(f'How many rows?'))
# CONNECT = int(input(f'How many to win?'))
# Decide on game type
# GAMETYPE = input(f'Graphics or Terminal? (g or t): ')

# Using a library to create a matrix that will represent the CONNECT 4 board
def create_board():
  board = numpy.zeros((HEIGHT, WIDTH))
  return board

def drop_piece(board, row, selection, piece):
  # Change the board location from a 0 to the value of the player that dropped the piece
  board[row][selection] = piece

def is_valid(board, selection):
  # Check if there is still space in that column, if not we cannot move here
  return board[HEIGHT - 1][selection] == 0

def open_row(board, selection):
  # r is for row, check from the bottom up for the next empty slot in that column
  for r in range(HEIGHT):
    # Return the first row that is empty
    if board[r][selection] == 0:
      return r

def print_board(board):
  # Flip the board so that it is the correct orientation, right side up
  # Using the numpy library
  print(numpy.flip(board, 0))

# Using the pygame library for the board
def draw_board(board):
  global half
  half = int(sq_size/2)
  # Draw the main body for the game, the empty holes
  for c in range(WIDTH):
    for r in range(HEIGHT):
      pygame.draw.rect(screen, (0, 0, 215), (c * sq_size + half, r * sq_size + sq_size, sq_size, sq_size))
      pygame.draw.circle(screen, (0, 0, 0), (c * sq_size + sq_size, r * sq_size + sq_size + half), half - 5)

  for c in range(WIDTH):
    for r in range(HEIGHT):    
      # Drawing the pieces placed
      if board[r][c] == 1:
        pygame.draw.circle(screen, (220, 0, 0), (c * sq_size + sq_size, HEIGHT * sq_size - r * sq_size + half), half - 5)
      elif board[r][c] == 2:
        pygame.draw.circle(screen, (0, 198, 0), (c * sq_size + sq_size, HEIGHT * sq_size - r * sq_size + half), half - 5)

  # Draw the yellow bars that hold up the game
  pygame.draw.rect(screen, (255, 250, 0), (half, sq_size, -16, HEIGHT * sq_size + sq_size))
  pygame.draw.rect(screen, (255, 250, 0), ((sq_size * WIDTH) + half, sq_size, 16, HEIGHT * sq_size + sq_size))

  # Update the playing board
  pygame.display.update()

# This is for CONNECT 4 specifically 
def win_move(board, piece):
  # c for column, r for row
  # Check for horizontal wins using double for loop to move through columns and rows
  for c in range(WIDTH - 3):
    for r in range(HEIGHT):
      if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
        return True

  # Check for vertical wins using double for loop
  for r in range(HEIGHT - 3):
    for c in range(WIDTH):
      if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
        return True

  # Check for right diagonal wins using double for loop
  for c in range(WIDTH - 3):
    for r in range(HEIGHT - 3):
      if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
        return True

  # Check for left diagonal
  for c in range(WIDTH - 3):
    for r in range(3, HEIGHT):
      if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
        return True

def win_move_select(board, row, selection, piece):
  # Dynamically check if the game is done, every move
  # Horizontal
  count = 0
  for c in range(WIDTH):
    if board[row][c] == piece:
      count += 1
    else:
      count = 0
    if count == CONNECT:
      return True
  
  # Vertical
  count = 0
  for r in range(HEIGHT):
    if board[r][selection] == piece:
      count += 1
    else:
      count = 0
    if count == CONNECT:
      return True

  # Forward Diagonal
  count = 0
  slot = -(CONNECT)
  for i in range(CONNECT * 2):
    # Check min WIDTH and HEIGHT
    while selection + slot < 0 or row + slot < 0:
      slot += 1

    # r = row, c = column
    r = row + slot
    c = selection + slot

    # Check for verticals
    if board[r][c] == piece:
      count += 1
      slot += 1
    else:
      count = 0
      slot += 1
    if count == CONNECT:
      return True
    # Stop the function
    if c >= WIDTH - 2 or r >= HEIGHT - 2:
      break

  # Backward Diagonal
  count = 0
  slot = CONNECT
  for i in range(CONNECT * 2):
    # Check min and max WIDTH and HEIGHT
    while selection - slot < 0 or row + slot >= HEIGHT:
      slot -= 1

    # r = row, c = column
    r = row + slot
    c = selection - slot

    # Check for verticals
    if board[r][c] == piece:
      count += 1
      slot -= 1
    else:
      count = 0
      slot -= 1
    if count == CONNECT:
      return True
    # Stop the function
    if c >= WIDTH - 1 or r < 0 + 1:
      break

def draw_game(board):
  # If the board has 1 empty space anywhere return false, otherwise true
  for c in range(WIDTH):
    for r in range(HEIGHT):
      if board[r][c] == 0:
        return False
  return True

# Initiators, creating the board, starting the game, and setting the turn
board = create_board()
# print_board(board)
gameInProgress = True
terminalGame = False
# if 'g' in GAMETYPE:
#   gameInProgress = True
#   terminalGame = False
# else:
#   terminalGame = True
#   gameInProgress = False
turn = 0

# Adding pygame for the hot graphics
pygame.init()
 
# Size of 1 individual piece
sq_size = 100
# Size of the board, adding space on the edges to breath and on the top and bottom for the extra piece currently in play
# and the text to display who's turn it is
brd_width = (WIDTH + 1) * sq_size
brd_height = (HEIGHT + 2) * sq_size

# Tuple for the display
size = (brd_width, brd_height)

screen = pygame.display.set_mode(size)
# Font for the display of messages
font_type = pygame.font.SysFont('Arial', 75)
draw_board(board)
pygame.display.update()
# Text for Diplaying who's turn it is at the bottom of the screen
go = font_type.render(f"Player 1's turn", 1, (255, 255, 255))
goTwo = font_type.render(f"Player 2's turn", 1, (255, 255, 255))
# Error text
err = font_type.render(f'Wrong Spot!', 1, (255, 255, 255))
# Winning Text
won = font_type.render(f'Congratulations Player 1!', 1, (255, 255, 255))
wonTwo = font_type.render(f'Congratulations Player 2!', 1, (255, 255, 255))
# Draw Text
draw = font_type.render(f'Tie Game!', 1, (255, 255, 255))

while gameInProgress:
  global half
  # Quit the game on exit
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      gameInProgress = False

    # Animation for piece about to be dropped
    if e.type == pygame.MOUSEMOTION:
      # Reset the top and bottom of the screen back to black
      pygame.draw.rect(screen, (0, 0, 0), (0, 0, brd_width, sq_size))
      pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
      # Grab the mouse position for the animation
      posX = e.pos[0]
      # Player 1 piece animation
      if turn % 2 == 0:
        pygame.draw.circle(screen, (220, 0, 0), (posX, half), half - 5)
        screen.blit(go, ((half * (WIDTH - 3)), (brd_height - sq_size) + 5))
      # Player 2 piece animation
      if turn % 2 != 0:
        pygame.draw.circle(screen, (0, 198, 0), (posX, half), half - 5)
        screen.blit(goTwo, ((half * (WIDTH - 3)), (brd_height - sq_size) + 5))

    pygame.display.update()

    # Game Logic for mouse clicks
    if e.type == pygame.MOUSEBUTTONDOWN:
      # Remove the current piece in case there is a draw or winner
      pygame.draw.rect(screen, (0, 0, 0), (0, 0, brd_width, sq_size))
      # Player 1's move
      if turn % 2 == 0:
        # Grab the position of the X-axis when the mouse is clicked
        posX = e.pos[0]
        selection = math.floor((posX - half)/sq_size)
        # Make sure the click is in the game area
        if selection > 6 or selection < 0:
          pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
          screen.blit(err, ((half * (WIDTH - 2)), (brd_height - sq_size) + 5))
        
        else:
          # Check if the input is a valid location
          # If valid we find the empty row and add the piece
          if is_valid(board, selection):
            row = open_row(board, selection)
            drop_piece(board, row, selection, 1)
            
            # Print the Board
            draw_board(board)
            # Check for a win
            if win_move_select(board, row, selection, 1):
              pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
              screen.blit(won, (half, 10))
              gameInProgress = False

          turn += 1
          # Display Player 2's turn
          pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
          screen.blit(goTwo, ((half * (WIDTH - 3)), (brd_height - sq_size) + 5))

      # Player 2's move
      elif turn % 2 != 0:
        posX = e.pos[0]
        selection = math.floor((posX - half)/sq_size)

        if selection > 6 or selection < 0:
          pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
          screen.blit(err, ((half * (WIDTH - 2)), (brd_height - sq_size) + 5))
        
        else:
          if is_valid(board, selection):
            row = open_row(board, selection)
            drop_piece(board, row, selection, 2)
          
            draw_board(board)
            if win_move_select(board, row, selection, 2):
              pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
              screen.blit(wonTwo, (half, 10))
              gameInProgress = False

          turn += 1
          # Display Player 1's turn
          pygame.draw.rect(screen, (0, 0, 0), (half, brd_height - sq_size, sq_size * WIDTH, sq_size))
          screen.blit(go, ((half * (WIDTH - 3)), (brd_height - sq_size) + 5))
      
      pygame.display.update()
  
  # Draw game instance
  if draw_game(board):
    screen.blit(draw, (half * (WIDTH - 2), 10))
    gameInProgress = False
  # Prevent instant closure of the game after a win
  if not gameInProgress:
    pygame.time.wait(5000)

# TERMINAL GAME LOGIC HERE!!#
while terminalGame:
  # Grab a move from Player 1
  if turn % 2 == 0:
    # By default input returns a string, wrap an int around it to get the number
    selection = int(input(f'Make a move player 1(0-{WIDTH}): '))

    # Set up a catch for the wrong input
    while selection > 6 or selection < 0:
      selection = int(input(f'Please input a value of/between 0 and {WIDTH}: '))

    # Check if the input is a valid location
    # If valid we find the empty row and add the piece
    if is_valid(board, selection):
      row = open_row(board, selection)
      drop_piece(board, row, selection, 1)

      # Print the Board
      print_board(board)
      # Check for a win
      if win_move_select(board, row, selection, 1):
        print(f'Congratulations Player 1!')
        terminalGame = False

  # Grab a move from Player 2
  elif turn % 2 != 0:
    selection = int(input(f'Your turn player 2(0-{WIDTH}): '))

    while selection > 6 or selection < 0:
      selection = int(input(f'Please input a value of/between 0 and {WIDTH}: '))

    if is_valid(board, selection):
      row = open_row(board, selection)
      drop_piece(board, row, selection, 2)

      print_board(board)

      if win_move_select(board, row, selection, 2):
        print(f'Congratulations Player 2!')
        terminalGame = False

  # Draw game instance
  if draw_game(board):
    terminalGame = False
    screen.blit(draw, (half * (WIDTH - 2), 10))

  turn += 1