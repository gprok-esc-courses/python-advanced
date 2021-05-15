from socket import *
import rsa

public_key, private_key = rsa.newkeys(512)

HOST = '127.0.0.1'
PORT = 21568
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

# Send the public key of the client
pk_bytes = public_key.save_pkcs1()
client_socket.send(pk_bytes)

# Read the server's public key
pk = client_socket.recv(1024).decode("utf8")
server_key = rsa.PublicKey.load_pkcs1(pk)
print(server_key)

# just to keep client alive
while True:
    pass

client_socket.close()
