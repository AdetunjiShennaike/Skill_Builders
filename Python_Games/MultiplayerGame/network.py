import socket

# Network class is responsible for connecting to the server
# Having it as a new file allows for it to be a reusable class/component
class Network:
  def __init__(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = '192.168.1.99'
    self.port = 3300
    self.address = (self.server, self.port)
    # Store the ID of the person connecting
    self.id = self.connect()
    print(self.id)

  def connect(self):
    try:
      self.client.connect(self.address)
      # After connecting, you should receive a encoded message, decode it and have it returned to become the ID
      return self.client.recv(2048).decode()
    except socket.error as err:
      print(err)
  
  def send(self, data):
    try:
      self.client.send(str.encode(data))
      return self.client.recv(2048).decode()
    except socket.error as err:
      print(err)


net = Network()
print(net.send('hello'))
print(net.send('working'))  