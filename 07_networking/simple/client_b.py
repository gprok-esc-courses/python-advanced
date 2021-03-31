from socket import *

HOST = '127.0.0.1'
PORT = 21567
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

while True:
    data_bytes = client_socket.recv(1024)
    if not data_bytes:
        break
    data = data_bytes.decode('utf-8')
    print(data)
    if data == "Bye...":
        break

client_socket.close()