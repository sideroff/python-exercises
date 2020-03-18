import socket
import time

from config import HOST, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    start = time.time()
    sock.send(b'1')
    resp = sock.recv(100)
    end = time.time()
    print(end-start)
    