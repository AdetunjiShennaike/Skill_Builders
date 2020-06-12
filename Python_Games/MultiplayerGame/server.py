import socket
from _thread import *
from player import Player
import sys
import pickle

server = '192.168.1.99'
PORT = 3300

# Af_inet and sock_stream are the type of connectionand how the string comes in
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  # Try to bind to the ip address that's given to the port
  sock.bind((server,PORT))
except socket.error as err:
  # If there is an error display the details
  str(err)

# Open the port to allow for client connections to happen
sock.listen(2)
print(f'Waiting for connetion, Server Started')

# A list of players in the match
players = [Player(100, 100, 50, 50, (0, 120, 0)), Player(0, 0, 50, 50, (210, 0, 0))]

def threaded(conn, player):
  # Checking for a threaded client
  # Send something back to the network so that we can tell if we connected to the client or not
  # What's being sent is the players initial position when first connecting
  pickle.dumps(conn.send(players[player]))
  reply = ''
  while True:
    try:
      # See if there is a signal for up to 2048 bits of data
      # If it is take convert it to a usable tuple
      data = pickle.loads(conn.recv(2048))
      # Set the users position to the received data
      players[player] = data

      if not data:
        print('Disconnected')
        break
      else:
        # Check which player just went so that you can send the right 
        # position back to move the player's piece
        if player == 1: 
          reply = players[0]
        else:
          reply = players[1]
        print(f'Received: {data}')
        print(f'Sending: {reply}')

      # Encode the information to send it over the internet
      conn.sendall(pickle.dumps(reply))

    except:
      break

  print('LOST Connection')
  conn.close()

# Setup logic for players connected and which player it is
currentPlayer = 0

while True:
  # Accept the incoming connection 
  conn, addr = sock.accept()
  # Display what address we are connected to
  print(f'Connected to: {addr}')

  # This runs another function in the background on start
  start_new_thread(threaded, (conn, currentPlayer))
  currentPlayer += 1