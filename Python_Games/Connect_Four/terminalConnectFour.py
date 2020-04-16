import numpy

# Using a library to create a matrix that will represent the connect 4 board
def create_board():
  global height, width
  # Board dimensions
  width = 7
  height = 6
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
  print(numpy.flip(board, 0))

# Initiators, creating the board, starting the game, and setting the turn
board = create_board()
print_board(board)
gameInProgress = True
turn = 0

while gameInProgress:
  # Grab a move from Player 1
  if turn % 2 == 0:
    # By default input returns a string, wrap an int around it to get the number
    selection = int(input(f'Make a move player 1(0-6):'))

    # Set up a catch for the wrong input
    while selection > 6 or selection < 0:
      selection = int(input(f'Please input a value of/between 0 and 6'))

    # Check if the input is a valid location
    # If valid we find the empty row and add the piece
    if is_valid(board, selection):
      row = open_row(board, selection)
      drop_piece(board, row, selection, 1)

  # Grab a move from Player 2
  elif turn % 2 != 0:
    selection = int(input(f'Your turn player 2(0-6):'))

    while selection > 6 or selection < 0:
      selection = int(input(f'Please input a value of/between 0 and 6'))

    if is_valid(board, selection):
      row = open_row(board, selection)
      drop_piece(board, row, selection, 2)

  print_board(board)
  turn += 1