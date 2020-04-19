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
  # Using the numpy library
  print(numpy.flip(board, 0))

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

# Initiators, creating the board, starting the game, and setting the turn
board = create_board()
print_board(board)
gameInProgress = True
turn = 0

while gameInProgress:
  global width
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
      if win_move(board, 1):
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

      if win_move(board, 2):
        print(f'Congratulations Player 2!')
        gameInProgress = False

  turn += 1