import socket

from config import HOST, PORT



# create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    serversocket.bind((HOST, PORT))
    serversocket.listen()
    
    print('socket listening on {}:{}'.format(socket.gethostname(), 80))
    
    clientsocket, addr = serversocket.accept()
    
    with clientsocket:
        print(f'{addr} has connected')
        print('{} has connected'.format(addr))
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            print('server recieved {}'.format(repr(data)))
            clientsocket.sendall(data)