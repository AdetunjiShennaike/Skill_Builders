import numpy

# Using a library to create a matrix that will represent the connect 4 board
def create_board():
  board = numpy.zeros((6, 7))
  return board


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
  if turn % 2 != 0:
    selection = int(input(f'Your turn player 2(0-6):'))

  turn += 1