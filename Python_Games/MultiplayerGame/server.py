import socket
from _thread import *
import sys

server = '192.168.1.250'
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

def threaded(conn):
  # 
  reply = ''
  while True:
    try:
      # See if there is a signal for up to 2048 bits of data
      data = conn.receive(2048)
      # Decode to unicode transformation format to make it rereadable
      reply = data.decode('utf-8')

      if not data:
        print('disconnected')
        break
      else:
        print(f'received: {reply}')

      # Encode the information to send it over the internet
      conn.sendall(str.encode(reply))

    except:
      break

while True:
  # Accept the incoming connection 
  conn, addr = sock.accept()
  # Display what address we are connected to
  print(f'Connected to: {addr}')

  # This runs another function in the background on start
  new_thread(threaded, (conn, ))