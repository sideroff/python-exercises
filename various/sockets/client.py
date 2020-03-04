import socket

from config import HOST, PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    clientsocket.connect((HOST, PORT))
    clientsocket.sendall(b'Hello world')
    data = clientsocket.recv(1024)

print('client recieved {}'.format(repr(data)))
