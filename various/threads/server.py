
from threading import Thread
import socket
import os

from config import HOST, PORT

connections = 0


def fib(n: int):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print(f'server listening on {HOST}:{PORT}')

        while True:
            connection, address = server.accept()
            with connection:
                print(f'connected by {address}')

                data = connection.recv(100)

                connection.sendall(bytes(fib(int(data))))

start_server()


# while True:
#     print(fib(int(input('n:'))))
