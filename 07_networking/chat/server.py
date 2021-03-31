import threading
from socket import *

HOST = '127.0.0.1'
PORT = 21568
ADDR = (HOST, PORT)


class Connection:
    def __init__(self, co, name):
        self.connection = co
        self.name = name



connections = []


def connection_thread(c):
    while True:
        data_bytes = c.connection.recv(1024)
        if not data_bytes:
            break
        print("Msg, " + c.name + ": " + data_bytes.decode())
        for con in connections:
            if con.name != c.name:
                con.connection.send(str.encode(c.name + ": ") + data_bytes)


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen()

while True:
    print('waiting for connection...')
    conn, addr = server_socket.accept()
    print('...connected from:', addr)
    name_bytes = conn.recv(1024)
    conn.send(b'Hi, start sending messages')
    connection = Connection(conn, name_bytes.decode())
    connections.append(connection)
    th = threading.Thread(target=connection_thread, args=(connection,))
    th.start()
    print(name_bytes.decode() + " thread started")


for c in connections:
    c.connection.send(b'Bye...')
    c.connection.close()
server_socket.close()
print("Server stopped ...")