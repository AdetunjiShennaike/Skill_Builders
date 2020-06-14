
class Game:
  def __init__(self, id):
    self.p1Go = False
    self.p2Go = False
    self.ready = False
    self.id = id
    self.moves =[None, None]
    self.wins = [0, 0]
    self.ties = 0

  # Return the players move selection
  def player_move(self, player):
    """
    :param player: [0,1]
    :return: move
    """

    return self.moves[player]

  # Check which player has made a move already and lock it in
  # this changes the false to true so that the game can continue
  def player(self, player, move):
    self.moves[player] = move
    if player == 0:
      self.p1Go = True
    if player == 1:
      self.p2Go = True

  def connected(self):
    return self.ready

  def bothGo(self):
    return self.p1Go and self.p2Go

  def winner(self):
    # Grab the first letter of each player's selection so 
    # you don't have to type out rock paper and scissor everytime
    pOne = self.moves[0].lower()[0]
    pTwo = self.moves[1].lower()[0]

    # Start at -1 in case there is a tie, we return -1
    winner = -1
    # player 1 is rock
    if pOne == 'r':
      if pTwo == 'p':
        winner = 1
      elif pTwo == 's':
        winner = 0
    # player 1 is paper
    elif pOne == 'p':
      if pTwo == 'r':
        winner = 0
      elif pTwo == 's':
        winner = 1
    # player 1 is scissors
    elif pOne == 's':
      if pTwo == 'r':
        winner = 1
      elif pTwo == 'p':
        winner = 0

    return winner

  # Reset the ready for both player to false
  def reset(self):
    self.p1Go = False
    self.p2Go = False