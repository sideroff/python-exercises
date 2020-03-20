from socket import *
from threading import Thread
import time

from config import HOST, PORT

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))

request_count = 0

def monitor():
    global request_count
    while True:    
        time.sleep(1)
        print(f'{request_count}/sec')
        request_count = 0

Thread(target=monitor).start()

def work():
    global request_count
    while True:
        sock.send(b'1')
        resp = sock.recv(100)
        request_count += 1

work()