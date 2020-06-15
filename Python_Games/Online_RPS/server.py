import socket
import pickle
from game import Game

server = ""
port = 3500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  str(e)

s.listen(2)
print(f'Waiting for ta connection, Server Started')


connected = set()
# games stores the separate instances of 1v1 rps matches
games = {}
# keeps track of the current id to keep from having duplicate game id's
idCount = 0

def threaded(conn, player, gameID):
  # grab idcount as a global reference so that we can keep consistency
  global idCount
  # send which player it is currently
  conn.send(str.encode(str(player)))

  reply = ""
  while True:
    data = conn.recv(4096).decode()

    # check if the current game exists still in the dictionary
    if gameID in games:
      game = games[gameID]

      # check what is received in the data and decide accordingly 
      if not data:
        break
      else:
        if data == 'reset':
          game.reset()
        elif data != 'get':
          game.play(player, data)

        reply = game
        conn.sendall(pickle.dumps(reply))


while True:
  conn, addr = s.accept()
  print(f'Connected to: {addr}')

  idCount += 1
  player = 0
  # increment by 1 for every two people, so every new game
  gameID = (idCount - 1)//2
  # create a new game instance for every 2 players
  if idCount % 2 == 1:
    games[gameID] = Game(gameID)
    print(f'Creating New Game...')
  else:
    # If we have an odd number than we set player to be the number 1(player 2)
    games[gameID].ready = True
    player = 1

  start_new_thread(threaded, (conn, player, gameID))