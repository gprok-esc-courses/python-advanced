import rsa

public_file = open("public.txt", "r")
public_data = public_file.read()
public_key = rsa.PublicKey.load_pkcs1(public_data, 'PEM')

private_file = open("private.txt", "r")
private_data = private_file.read()
private_key = rsa.PrivateKey.load_pkcs1(private_data, 'PEM')

print(public_key)
print(private_key)

message = 'Hello World!'
message_bytes = message.encode('utf8')
message_enc = rsa.encrypt(message_bytes, public_key)

print(message_enc)

msg_bytes = rsa.decrypt(message_enc, private_key)
msg = msg_bytes.decode('utf8')

print(msg)