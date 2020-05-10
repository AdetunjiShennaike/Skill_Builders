import socket


class Network:
  def __init__(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = '192.168.1.250'
    self.port = 3300
    self.address = (self.server, self.port)
    self.id = self.connect()
    print(self.id)

  def connect(self):
    try:
      self.client.connect(self.address)
      return self.client.recv(2048).decode()
    except:
      pass