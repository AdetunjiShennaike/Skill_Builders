import numpy
import pygame

# Using a library to create a matrix that will represent the connect 4 board
def create_board():
  global height, width, connect
  # Board dimensions
  width = 7
  height = 6
  connect = 4
  # Dynamic
  # width = int(input(f'How many columns?'))
  # height = int(input(f'How many rows?'))
  # connect = int(input(f'How many to win?'))

  # Decide on game type
  game_type = input(f'Graphics or Terminal? ')
  board = numpy.zeros((height, width))
  return board

def drop_piece(board, row, selection, piece):
  # Change the board location from a 0 to the value of the player that dropped the piece
  board[row][selection] = piece

def is_valid(board, selection):
  global height
  # Check if there is still space in that column, if not we cannot move here
  return board[height - 1][selection] == 0

def open_row(board, selection):
  global height
  # r is for row, check from the bottom up for the next empty slot in that column
  for r in range(height):
    # Return the first row that is empty
    if board[r][selection] == 0:
      return r

def print_board(board):
  # Flip the board so that it is the correct orientation, right side up
  # Using the numpy library
  print(numpy.flip(board, 0))

# Using the pygame library for the board
def draw_board(board):
  pass

# This is for connect 4 specifically 
def win_move(board, piece):
  global width, height
  # c for column, r for row
  # Check for horizontal wins using double for loop to move through columns and rows
  for c in range(width - 3):
    for r in range(height):
      if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
        return True

  # Check for vertical wins using double for loop
  for r in range(height - 3):
    for c in range(width):
      if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
        return True

  # Check for right diagonal wins using double for loop
  for c in range(width - 3):
    for r in range(height - 3):
      if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
        return True

  # Check for left diagonal
  for c in range(width - 3):
    for r in range(3, height):
      if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
        return True

def win_move_select(board, row, selection, piece):
  global width, height, connect
  # Dynamically check if the game is done, every move
  # Horizontal
  count = 0
  for c in range(width):
    if board[row][c] == piece:
      count += 1
    else:
      count = 0
    if count == connect:
      return True
  
  # Vertical
  count = 0
  for r in range(height):
    if board[r][selection] == piece:
      count += 1
    else:
      count = 0
    if count == connect:
      return True

  # Forward Diagonal
  count = 0
  slot = -(connect)
  for i in range(connect * 2):
    # Check min width and height
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
    if count == connect:
      return True
    # Stop the function
    if c >= width - 1 or r >= height - 1:
      break

  # Backward Diagonal
  count = 0
  slot = connect
  for i in range(connect * 2):
    # Check min and max width and height
    while selection - slot < 0 or row + slot >= height:
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
    print(r, c, count)
    if count == connect:
      return True
    # Stop the function
    if c >= width - 1 or r <= 0 + 1:
      break


# Initiators, creating the board, starting the game, and setting the turn
board = create_board()
print_board(board)
gameInProgress = True
# if 'graphics' in game_type:
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
brd_width = (width + .5) * sq_size
brd_height = (height + 2) * sq_size

# Tuple for the display
size = (width, height)

screen = pygame.display.set_mode(size)

while gameInProgress:
  global width

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
    
    if e.type == pygame.MOUSEBUTTONDOWN:
    


# TERMINAL GAME LOGIC HERE!!#
while terminalGame:
  # Grab a move from Player 1
  if turn % 2 == 0:
    # By default input returns a string, wrap an int around it to get the number
    selection = int(input(f'Make a move player 1(0-{width}): '))

    # Set up a catch for the wrong input
    while selection > 6 or selection < 0:
      selection = int(input(f'Please input a value of/between 0 and {width}: '))

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
        gameInProgress = False

  # Grab a move from Player 2
  elif turn % 2 != 0:
    selection = int(input(f'Your turn player 2(0-{width}): '))

    while selection > 6 or selection < 0:
      selection = int(input(f'Please input a value of/between 0 and {width}: '))

    if is_valid(board, selection):
      row = open_row(board, selection)
      drop_piece(board, row, selection, 2)

      print_board(board)

      if win_move_select(board, row, selection, 2):
        print(f'Congratulations Player 2!')
        gameInProgress = False

  turn += 1