import socket
from _thread import *
import sys

server = '192.168.1.250'
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

def threaded(conn):
  # Checking for a threaded client
  # Send something back to the network so that we can tell if we connected to the client or not
  conn.send(str.encode("Connected"))
  reply = ''
  while True:
    try:
      # See if there is a signal for up to 2048 bits of data
      data = conn.receive(2048)
      # Decode to unicode transformation format to make it rereadable
      reply = data.decode('utf-8')

      if not data:
        print('Disconnected')
        break
      else:
        print(f'Received: {reply}')

      # Encode the information to send it over the internet
      conn.sendall(str.encode(reply))

    except:
      break

  print('LOST Connection')
  conn.close()

while True:
  # Accept the incoming connection 
  conn, addr = sock.accept()
  # Display what address we are connected to
  print(f'Connected to: {addr}')

  # This runs another function in the background on start
  new_thread(threaded, (conn, ))