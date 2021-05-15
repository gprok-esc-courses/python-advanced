import threading
from socket import *

import rsa

public_key, private_key = rsa.newkeys(512)

HOST = '127.0.0.1'
PORT = 21568
ADDR = (HOST, PORT)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen()
print('waiting for connection...')

conn, addr = server_socket.accept()
print('...connected from:', conn, addr)

# Receive key from the client as text and convert to actual key
pk = conn.recv(1024).decode("utf8")
client_key = rsa.PublicKey.load_pkcs1(pk)
print(client_key)

# Send the public key to the client
pk_bytes = public_key.save_pkcs1()
conn.send(pk_bytes)

# just to keep server alive
while True:
    pass

server_socket.close()
