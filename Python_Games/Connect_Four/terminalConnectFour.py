import numpy

# Using a library to create a matrix that will represent the connect 4 board
def create_board():
  board = numpy.zeros((6, 7))
  return board

board = create_board()
print(board)