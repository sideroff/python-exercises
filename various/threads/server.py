# you can test the server by running
# nc <host> <port>
# <any number>

from socket import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor

from config import HOST, PORT

pool = ProcessPoolExecutor(5)

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    print(f'listening on {HOST}:{PORT}')
    while True:
        client, addr = sock.accept()
        print(f'connected by {addr}')


        # runs the handler synchronously so one client can be served at a time
        # fib_handler(client,addr)

        # runs the target function in a thread so more clients can be served, but is limited by GIL
        # so any CPU work will throttle the server response time
        Thread(target=fib_handler, args=(client, addr), daemon=True).start()

def fib_handler(client, addr):
    while True:
        req = client.recv(100)

        if not req:
            break
        
        n = int(req)

        # default way is to calculate work ( limited by gil )
        result = fib(n)

        # you can mitigate the server throttling because of CPU work
        # is to use process pools, but then you have the overhead of de/serialization
        future = pool.submit(fib, n)
        result = future.result()
        
        # print(f'{addr[-1]}: fib({n}) = {result}')
        
        response = str(result).encode('ascii') + b'\n'
        client.send(response)

def fib(n: int):
    if n < 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)



fib_server((HOST, PORT))