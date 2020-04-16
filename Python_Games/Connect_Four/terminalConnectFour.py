import numpy

# Using a library to create a matrix that will represent the connect 4 board
def create_board():
  global top, width
  width = 7
  top = 6
  board = numpy.zeros((top, width))
  return board

def drop_piece():
  pass

def is_valid(board, selection):
  global top
  # Check if there is still space in that column, if not we cannot move here
  return board[top][selection] == 0

def get_next_open_row():
  pass

# Initiators, creating the board, starting the game, and setting the turn
board = create_board()
gameInProgress = True
turn = 0

while gameInProgress:
  # Grab a move from Player 1
  if turn % 2 == 0:
    # By default input returns a string, wrap an int around it to get the number
    selection = int(input(f'Make a move player 1(0-6):'))

  # Grab a move from Player 2
  elif turn % 2 != 0:
    selection = int(input(f'Your turn player 2(0-6):'))

  # Set up a catch for the wrong input
  while selection > 6 or selection < 0:
    selection = int(input(f'Please input a value of/between 0 and 6'))
  turn += 1