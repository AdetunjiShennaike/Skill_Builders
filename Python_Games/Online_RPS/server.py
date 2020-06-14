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

def threaded(conn, player, gameID):
  pass

while True:
  conn, addr = s.accept()
  print(f'Connected to: {addr}')

  start_new_thread(threaded, (conn))