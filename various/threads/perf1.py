from socket import * 
import time

from config import HOST, PORT

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST,PORT))

# send requests back to back to see how much time it takes for the server to respond
while True:
    start = time.time()

    sock.send(b'30')
    resp = sock.recv(100)
    
    end = time.time()
    print(end-start)