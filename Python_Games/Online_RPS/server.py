import socket
import pickle
from game import Game
from _thread import *

server = "192.168.1.99"
port = 3500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  str(e)

s.listen()
print(f'Waiting for a connection, Server Started')


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
    # try to decode the data sent by the network
    try:
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

          # reply with the current point in the game it is at
          reply = game
          conn.sendall(pickle.dumps(reply))

      else:
        break
    except Exception as err:
      print(err)

  # if you break and exit the game start a leaving sequence 
  # delete the game from the dictionary and send a message that the game is closing
  print(f'Lost connection')
  try:
    del games[gameID]
    print(f'Closing Game {gameID}')
  except:
    pass

  idCount -= 1
  conn.close()

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