
class Game:
  def __init__(self, id):
    self.p1Go = False
    self.p2Go = False
    self.ready = False
    self.id = id
    self.moves =[None, None]
    self.wins = [0, 0]
    self.ties = 0

  def player_move(self, player):
    """
    :param player: [0,1]
    :return: move
    """

    return self.moves[player]

  def player(self, player, move):
    self.moves[player] = move
    if player == 0:
      self.p1Go = True
    if player == 1:
      self.p2Go = True