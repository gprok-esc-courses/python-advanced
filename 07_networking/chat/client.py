import threading
from socket import *


def client_thread(c):
    while True:
        data_bytes = c.recv(1024)
        data = data_bytes.decode()
        print(data)


HOST = '127.0.0.1'
PORT = 21568
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

name = input('name:')
client_socket.send(str.encode(name))

th = threading.Thread(target=client_thread, args=(client_socket,))
th.start()

while True:
    data = input('> ')
    data_bytes = str.encode(data)
    if not data:
        continue
    client_socket.send(data_bytes)

client_socket.close()
