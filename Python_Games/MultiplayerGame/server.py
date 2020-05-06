import socket
import threading
import sys

server = ''
PORT = 3300

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  sock.bind((server,PORT))
except socket.error as err:
  str(err)

# Open the port to allow for connections to happen
sock.listen(2)