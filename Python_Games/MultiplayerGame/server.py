import socket
import threading
import sys

server = ''
PORT = 3300

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

def thread(conn):
  # 
  pass

while True:
  # Accept the incoming connection 
  conn, addr = sock.accept()
  # Display what address we are connected to
  print(f'Connected to: {addr}')